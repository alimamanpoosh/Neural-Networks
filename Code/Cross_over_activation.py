def crossover_activation(parent1, parent2):
    parent1 , parent2 = parent2 , parent1
    return parent1 , parent2
# print (crossover_bw(10, 20, 10))
temp = [{'feature extraction': 3, 'hidden layer': [30], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [20, 20], 'activation function': 2}]
print(crossover_activation(temp[0]['activation function'], temp[2]['activation function']))
# input ==> (1, 2)
# output ==> (2, 1)