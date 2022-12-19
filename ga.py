import os
import io
import json
import random
import argparse
import matplotlib.pyplot as plt
from ops.GACrossover import ordered_crossover
from ops.GAMutation import mutate
from ops.plotRoute import plot_route
import time

random.seed(0)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default=".\data\json\homberger_200_customer_instances\c1_2_1.json", required=False,
                        help="Enter the input Json file name")
    parser.add_argument('--pop_size', type=int, default=50, required=False,
                        help="Enter the population size")
    parser.add_argument('--mute_prob', type=float, default=0.5, required=False,
                        help="Mutation Probabilty")
    parser.add_argument('--iterations', type=int, default=1000, required=False,
                        help="Number of iterations to run")

    return parser.parse_args()


def load_instance(json_file):
    """
    Inputs: path to json file
    Outputs: json file object if it exists, or else returns NoneType
    """
    if os.path.exists(path=json_file):
        with io.open(json_file, 'rt', newline='') as file_object:
            return json.load(file_object)
    return None


def initialize_population(n_customers, n_population):
    population = []
    while len(population) < n_population:
        chromosome = random.sample([i for i in range(1, n_customers+1)], n_customers)
        if chromosome not in population:
            population.append(chromosome)
    return population

# -> new vehicle when max capacity
def evaluate(chromosome, distance_matrix, demand, cap_vehicle, return_subroute=False):
    total_distance = 0
    cur_load = 0
    n_vehicle = 0
    route = []
    sub_route = []
    for customer in chromosome:
        cur_load += demand[customer]
        if cur_load > cap_vehicle:
            if return_subroute:
                sub_route.append(route[:])
            total_distance += calculate_distance(route, distance_matrix)
            n_vehicle += 1
            cur_load = demand[customer]
            route = [customer]
        else:
            route.append(customer)

    total_distance += calculate_distance(route, distance_matrix)
    n_vehicle += 1
    
    if return_subroute:
        sub_route.append(route[:])
        return sub_route
    return total_distance + n_vehicle


def calculate_distance(route, distance_matrix):
    distance = 0
    distance += distance_matrix[0][route[0]]
    distance += distance_matrix[route[-1]][0]
    for i in range(0, len(route)-1):
        distance += distance_matrix[route[i]][route[i+1]]
    return distance


def get_chromosome(population, func, *params, reverse=False, k=1):
    scores = []
    for chromosome in population:
        scores.append([func(chromosome, *params), chromosome])
    scores.sort(reverse=reverse)
    if k == 1:
        return scores[0]
    elif k > 1:
        return scores[:k]
    else:
        raise Exception("invalid k")
 
def replace(population, chromo_in, chromo_out):
    population[population.index(chromo_out)] = chromo_in


def check_validity(chromosome, length):
    for i in range(1, length+1):
        if i not in chromosome:
            raise Exception("invalid chromosome")


if __name__ == '__main__':

    # get input
    # initialize population
    # calculate cost
    # if terminal -> finish
    # repeat iteration
    # -> select chromosomes
    # -> mutate chromosomes
    # -> replace
    # -> calculate cost
    
    # record start time
    start = time.time()
    
    args = get_parser()
    instance = load_instance(args.input_path)
    n_customers = instance['Number_of_customers']
    demand = {}
    for i in range(1, n_customers+1):
        demand[i] = instance["customer_" + str(i)]['demand']

    distance_matrix = instance['distance_matrix']
    cap_vehicle = instance['vehicle_capacity']
    depart = instance['depart']
    n_population = args.pop_size
    iteration = args.iterations
    cur_iter = 1
    mutate_prob = args.mute_prob

    population = initialize_population(n_customers, n_population)
    prev_score, chromosome = get_chromosome(population, evaluate, distance_matrix, demand, cap_vehicle)

    score_history = [prev_score]

    while cur_iter <= iteration:
        # -> Start GA
        chromosomes = get_chromosome(population, evaluate, distance_matrix, demand, cap_vehicle, k=2)
        chromosome1 = chromosomes[0][1]
        chromosome2 = chromosomes[1][1]
        
        # -> can change to single_point_crossover(chromo1,chromo2,points:int)  
        # -> can change to multi_point_crossover(chromo1,chromo2,points:int)
        # -> can change to uniform_crossover(chromo1, chromo2, crossover_prob:float) 
        # -> detail in GACrossover.py
        offspring1, offspring2 = ordered_crossover(chromosome1, chromosome2)
        
        # -> Mutation
        offspring1 = mutate(offspring1, mutate_prob)
        offspring2 = mutate(offspring2, mutate_prob)
        score1 = evaluate(offspring1, distance_matrix, demand, cap_vehicle)
        score2 = evaluate(offspring2, distance_matrix, demand, cap_vehicle)
        score, chromosome = get_chromosome(population, evaluate, distance_matrix, demand, cap_vehicle, reverse=True)

        if score1 < score:
            replace(population, chromo_in=offspring1, chromo_out=chromosome)

        score, chromosome = get_chromosome(population, evaluate, distance_matrix, demand, cap_vehicle, reverse=True)

        if score2 < score:
            replace(population, chromo_in=offspring2, chromo_out=chromosome)

        score, chromosome = get_chromosome(population, evaluate, distance_matrix, demand, cap_vehicle)
        score_history.append(score)
        prev_score = score
        print(f"Iteration : {cur_iter}")
        cur_iter += 1

    print(score, chromosome)
    subroutes = evaluate(chromosome, distance_matrix, demand, cap_vehicle, return_subroute=True)
    
    # record end time
    end = time.time()
    # print the difference between start
    # and end time in milli. secs
    print("The time of execution of above program is :", (end-start) * 10**3, "ms")
    
    # -> Save rinning time(ms) in txt file
    f = open("runningtime.txt", "a")
    f.write(f"running time : {(end-start)* 10**3} ms \n")
    f.close()
    
    # Plot Graph
    title = f"SSGA with CVRP, mute_prob={mutate_prob}"
    plot_route(subroutes, instance, title)
    plt.cla()
    plt.plot(score_history)
    plt.xlabel("Iterations")
    plt.ylabel("Cost")
    plt.title(title)
    plt.savefig('figure/cost.png')
    plt.show()

