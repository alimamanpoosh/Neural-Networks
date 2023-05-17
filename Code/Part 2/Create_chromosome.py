import random

type_feature_extraction = "feature extraction"
hidden_layer = "hidden layer"
type_activation_function = "activation function"

def create_chromosome1():
    chromosome = []
    num_gens = 6
    for i in range(num_gens):
        gen = dict()
        gen[type_feature_extraction] = random.randint(1,3)
        # num_hidden_layer = random.randint(0, 3)
        # # gen[num_hidden_layer] = (random.uniform(0, 20), random.uniform(0, 20))
        # for j in range(num_hidden_layer):
        #     hiddenLayer = []
        #     temp = random.choice([10, 20, 30])
        #     hiddenLayer.append(temp)
        #     # create the random neuron 10 or 20 or 30 and append to hiddenLayer
        # gen[hidden_layer] = hiddenLayer
        num_hidden_layer = random.randint(0, 2)
        gen[hidden_layer] = [random.choice([10, 20, 30]) for _ in range(num_hidden_layer)]
        gen[type_activation_function] = [random.choice([1, 2]) for _ in range(num_hidden_layer+1)]
            


        chromosome.append(gen)
    return chromosome
print(create_chromosome1())


# if num gens = 10

# if num gens = 6

temp6 = [{'feature extraction': 1, 'hidden layer': [20], 'activation function': [1, 2]}, {'feature extraction': 1, 'hidden layer': [], 'activation function': [2]}, {'feature extraction': 3, 'hidden layer': [10], 'activation function': [2, 1]}, {'feature extraction': 1, 'hidden layer': [30], 'activation function': [2, 2]}, {'feature extraction': 3, 'hidden layer': [20, 20], 'activation function': [2, 2, 2]}, {'feature extraction': 1, 'hidden layer': [20, 30], 'activation function': [1, 1, 1]}]