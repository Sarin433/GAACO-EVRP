import random

def mutate(chromosome, probability):
    if random.random() < probability:
        index1, index2 = random.sample(range(len(chromosome)), 2)
        chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]
        index1, index2 = sorted(random.sample(range(len(chromosome)), 2))
        mutated = chromosome[:index1] + list(reversed(chromosome[index1:index2+1]))
        if index2 < len(chromosome) - 1:
            mutated += chromosome[index2+1:]
        return mutated
    return chromosome