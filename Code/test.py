def crossover_blocks(parent1, parent2):
    return parent2, parent1
    # crossover_point = int(random.uniform(0, 1) * len(parent1))
    # p = random.randint(0, 1)
    # if p == 0:
    #     offspring1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    #     offspring2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    # else:
    #     offspring1 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    #     offspring2 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    #
    # return offspring1.tolist(), offspring2.tolist()


def crossover_tower(parent1, parent2, alpha=0.25):  # tuple type   (sample crossover)   (20 - 30 )  sub 10 ==> alpha 0.25 ==> (22.5-27.5)
    parent1 = list(parent1)
    parent2 = list(parent2)
    sub_x = abs(parent1[0] - parent2[0])
    sub_y = abs(parent1[1] - parent2[1])
    amount_of_change_x = alpha * sub_x
    amount_of_change_y = alpha * sub_y

    if parent2[0] < parent1[0]:
        parent1[0] -= amount_of_change_x
        parent2[0] += amount_of_change_x
    else:
        parent1[0] += amount_of_change_x
        parent2[0] -= amount_of_change_x

    if parent2[1] < parent1[1]:
        parent1[1] -= amount_of_change_y
        parent2[1] += amount_of_change_y
    else:
        parent1[1] += amount_of_change_y
        parent2[1] -= amount_of_change_y

    offspring1 = (parent1[0], parent1[1])
    offspring2 = (parent2[0], parent2[1])

    return offspring1, offspring2


def crossover_bw(parent1, parent2, num_of_blocks, alpha=0.25):  # we use avg replace that  (blend crossover) (20 - 30 )   random (17.5 - 32.5)
    # parent1 ===>  gen 1
    # parent2 ===>  gen 2

    # """Perform crossover blend on two decimal numbers."""
    d = abs(parent1 - parent2)
    result0 = random.uniform(parent1 - alpha * d, parent2 + alpha * d)
    result1 = random.uniform(parent1 - alpha * d, parent2 + alpha * d)

    result2 = random.uniform(parent2 - alpha * d, parent1 + alpha * d)
    result3 = random.uniform(parent2 - alpha * d, parent1 + alpha * d)

    minimum = smallest_neighborhood * min_speed * num_of_blocks

    if parent2 > parent1:
        if result0 < minimum and result1 < minimum:
            return (minimum, minimum)
        elif result0 < minimum and result1 > minimum:
            return (minimum, result1)
        elif result0 > minimum and result1 < minimum:
            return (result0, minimum)
        else:
            return (result0, result1)
        # return random.uniform(parent1 - alpha * d, parent2 + alpha * d), random.uniform(parent1 - alpha * d, parent2 + alpha * d)
    else:
        if result2 < minimum and result3 < minimum:
            return (minimum, minimum)
        elif result2 < minimum and result3 > minimum:
            return (minimum, result3)
        elif result2 > minimum and result3 < minimum:
            return (result2, minimum)
        else:
            return (result2, result3)


def crossover(chro1, chro2):
    child1, child2 = copy.deepcopy(chro1), copy.deepcopy(chro2)
    for i in range(len(child1)):
        child1[i][blocks], child2[i][blocks] = crossover_blocks(child1[i][blocks], child2[i][blocks])

        # for j in range(len(child1[i][blocks])):
        #     for gen1, gen2 in zip(child1, child2):
        #         if gen1 is not child1[i]:
        #             if child1[i][blocks][j] in gen1[blocks]:
        #                 k = gen1[blocks].index(child1[i][blocks][j])
        #                 gen1[blocks][k] = child2[i][blocks][j]
        #         elif gen1[blocks].count(child1[i][blocks][j]) > 1:
        #             k = gen1[blocks].index(child1[i][blocks][j])
        #             gen1[blocks][k] = child2[i][blocks][j]
        #
        #         if gen2 is not child2[i]:
        #             if child2[i][blocks][j] in gen2[blocks]:
        #                 k = gen2[blocks].index(child2[i][blocks][j])
        #                 gen2[blocks][k] = child1[i][blocks][j]
        #         elif gen2[blocks].count(child2[i][blocks][j]) > 1:
        #             k = gen2[blocks].index(child2[i][blocks][j])
        #             gen2[blocks][k] = child1[i][blocks][j]

        child1[i][location], child2[i][location] = crossover_tower(child1[i][location], child2[i][location])

        child1[i][BW], child2[i][BW] = crossover_bw(child1[i][BW], child2[i][BW], len(child1[i][blocks]))

    return child1, child2