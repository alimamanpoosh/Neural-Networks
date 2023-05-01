def crossover_feature(parent1, parent2):
    parent1 , parent2 = parent2 , parent1
    return parent1 , parent2

temp = [{'feature extraction': 3, 'hidden layer': [30], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [20, 20], 'activation function': 2}]

print(crossover_feature(temp[0]['feature extraction'], temp[1]['feature extraction']))
# input ==> (3, 2)
# output ==> (2, 3)