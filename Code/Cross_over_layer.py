def crossover_feature(parent1, parent2):
    if len(parent1) > len(parent2):
        parent1 , parent2 = parent2 , parent1
    pass    
temp = [{'feature extraction': 3, 'hidden layer': [30], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [20, 20], 'activation function': 2}]

patent1 = temp[0]['hidden layer'] 
parent2 = temp[1]['hidden layer']

print(patent1, parent2)
print(len(parent2))