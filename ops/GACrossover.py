import numpy as np
import random

def single_point_crossover(chromo1,chromo2,points):
    # onePoints = random.randint(0,min(len(chromo1),len(chromo2)))
    ind1_new = np.append(chromo1[:points], chromo2[points:])
    ind2_new = np.append(chromo2[:points], chromo1[points:])
    return list(ind1_new), list(ind2_new)

def multi_point_crossover(chromo1,chromo2,points):
    randomPoints = sorted(random.sample(range(0, min(len(chromo1),len(chromo2))), points))
    for i in randomPoints:
        chromo1, chromo2 = single_point_crossover(chromo1,chromo2,i)
    return list(chromo1), list(chromo2)

def ordered_crossover(chromo1, chromo2):
    # Modifying this to suit our needs
    #  If the sequence does not contain 0, this throws error
    #  So we will modify inputs here itself and then
    #       modify the outputs too

    ind1 = [x-1 for x in chromo1]
    ind2 = [x-1 for x in chromo2]
    size = min(len(ind1), len(ind2))
    a, b = random.sample(range(size), 2)
    if a > b:
        a, b = b, a

    holes1, holes2 = [True] * size, [True] * size
    for i in range(size):
        if i < a or i > b:
            holes1[ind2[i]] = False
            holes2[ind1[i]] = False

    # We must keep the original values somewhere before scrambling everything
    temp1, temp2 = ind1, ind2
    k1, k2 = b + 1, b + 1
    for i in range(size):
        if not holes1[temp1[(i + b + 1) % size]]:
            ind1[k1 % size] = temp1[(i + b + 1) % size]
            k1 += 1

        if not holes2[temp2[(i + b + 1) % size]]:
            ind2[k2 % size] = temp2[(i + b + 1) % size]
            k2 += 1

    # Swap the content between a and b (included)
    for i in range(a, b + 1):
        ind1[i], ind2[i] = ind2[i], ind1[i]

    # Finally adding 1 again to reclaim original input
    ind1 = [x+1 for x in ind1]
    ind2 = [x+1 for x in ind2]
    return ind1, ind2