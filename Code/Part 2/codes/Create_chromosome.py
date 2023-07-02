import random

type_feature_extraction = "feature extraction"
hidden_layer = "hidden layer"
type_activation_function = "activation function"

def create_chromosomes(num_chromosomes):
    chromosomes = []
    for i in range(num_chromosomes):
        chro = dict()
        chro[type_feature_extraction] = random.randint(1,3)
        num_hidden_layer = random.randint(0, 2)
        chro[hidden_layer] = [random.choice([10, 20, 30]) for _ in range(num_hidden_layer)]
        chro[type_activation_function] = [random.choice([1, 2]) for _ in range(num_hidden_layer + 1)]
        chromosomes.append(chro)
    return chromosomes
print(create_chromosomes())


# if num gens = 10

# if num gens = 6

temp6 = [{'feature extraction': 1, 'hidden layer': [20], 'activation function': [1, 2]}, {'feature extraction': 1, 'hidden layer': [], 'activation function': [2]}, {'feature extraction': 3, 'hidden layer': [10], 'activation function': [2, 1]}, {'feature extraction': 1, 'hidden layer': [30], 'activation function': [2, 2]}, {'feature extraction': 3, 'hidden layer': [20, 20], 'activation function': [2, 2, 2]}, {'feature extraction': 1, 'hidden layer': [20, 30], 'activation function': [1, 1, 1]}]