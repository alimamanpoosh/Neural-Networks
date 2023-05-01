def crossover_feature(parent1, parent2):
    parent1_len = len(parent1)
    parent2_len = len(parent2)
    
    if parent1_len == 0 and parent2_len == 1:
        value = parent2.pop()
        parent1.append(value)
    elif parent1_len == 1 and parent2_len == 0:
        value = parent1.pop()
        parent2.append(value)
    elif parent1_len == 1 and parent2_len == 1:
        parent1[0], parent2[0] = parent2[0], parent1[0]
    elif parent1_len == 1 and parent2_len == 2:
        value = parent2.pop()
        parent1.append(value)
    elif parent1_len == 2 and parent2_len == 1:
        value = parent1.pop()
        parent2.append(value)
    elif parent1_len >= 3 and parent2_len >= 2:
        parent1[2:], parent2[2:] = parent2[2:], parent1[2:]
    elif parent1_len == 2 and parent2_len == 3:
        value = parent2.pop()
        parent1.append(value)
    elif parent1_len == 3 and parent2_len == 1:
        value_1 = parent1.pop()
        value_2 = parent1.pop()
        parent2.append(value_1)
        parent2.append(value_2)
    elif parent1_len == 1 and parent2_len == 3:
        value_1 = parent2.pop()
        value_2 = parent2.pop()
        parent1.append(value_1)
        parent1.append(value_2)
    
    
    return parent1, parent2
       
temp = [{'feature extraction': 3, 'hidden layer': [30], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [20, 20], 'activation function': 2}]

parent1 = temp[0]['hidden layer'] 
parent2 = temp[2]['hidden layer']

print("parent1: ",parent1,"parent2: ", parent2)
child1, child2 = crossover_feature(parent1, parent2)
print("child1: ", child1,"child2: ", child2)

temp2 = [{'feature extraction': 1, 'hidden layer': [20, 30, 30], 'activation function': 2}, {'feature extraction': 2, 'hidden layer': [30, 10], 'activation function': 1}, {'feature extraction': 1, 'hidden layer': [], 'activation function': 2}, {'feature extraction': 1, 'hidden layer': [10], 'activation function': 1}, {'feature extraction': 3, 'hidden layer': [10, 30, 10], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [20, 30, 20], 'activation function': 1}, {'feature extraction': 3, 'hidden layer': [30, 20, 20], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [10, 10], 'activation function': 1}, {'feature extraction': 2, 'hidden layer': [20], 'activation function': 1}, {'feature extraction': 1, 'hidden layer': [], 'activation function': 1}]

