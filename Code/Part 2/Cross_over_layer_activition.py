def crossover_layer_activation(parent1_layer, parent2_layer, parent1_active, parent2_active):
    parent1_len = len(parent1_layer)
    parent2_len = len(parent2_layer)
    
    if parent1_len - parent2_len == -1:
        value = parent2_layer.pop()
        parent1_layer.append(value)
        value = parent2_active.pop()
        parent1_active.append(value)

    elif parent1_len - parent2_len == 1:
        value = parent1_layer.pop()
        parent2_layer.append(value)
        value = parent1_active.pop()
        parent2_active.append(value)

    elif parent1_len == parent2_len :
        parent1_layer[-1], parent2_layer[-1] = parent2_layer[-1], parent1_layer[-1]
        parent1_active[-1], parent2_active[-1] = parent2_active[-1], parent1_active[-1]

    else:
        for i in range(int(abs(parent1_len-parent2_len)/2)):
            if parent2_len >parent1_len:
                value = parent2_layer.pop()
                parent1_layer.append(value)
                value = parent2_active.pop()
                parent1_active.append(value)
            else:
                value = parent1_layer.pop()
                parent2_layer.append(value)
                value = parent1_active.pop()
                parent2_active.append(value)
    
    
    return parent1_layer, parent2_layer, parent1_active, parent2_active
       

temp = [{'feature extraction': 1, 'hidden layer': [20], 'activation function': [1, 2]}, {'feature extraction': 1, 'hidden layer': [], 'activation function': [2]}, {'feature extraction': 3, 'hidden layer': [10], 'activation function': [2, 1]}, {'feature extraction': 1, 'hidden layer': [30], 'activation function': [2, 2]}, {'feature extraction': 3, 'hidden layer': [20, 20], 'activation function': [2, 2, 2]}, {'feature extraction': 1, 'hidden layer': [20, 30], 'activation function': [1, 1, 1]}]

parent1_layer = temp[0]['hidden layer'] 
parent2_layer = temp[4]['hidden layer']
parent1_active = temp[0]['activation function']
parent2_active = temp[4]['activation function']
print("parent1_layer: ",parent1_layer,"parent2_layer: ", parent2_layer , "parent1_active: ", parent1_active, "parent2_active: ", parent2_active)


child1_layer, child2_layer, child1_active, child2_active = crossover_layer_activation(parent1_layer, parent2_layer, parent1_active, parent2_active)


print("child1_layer: ", child1_layer,"child2_layer: ", child2_layer , "child1_active: ", child1_active, "child2_active: ", child2_active)

