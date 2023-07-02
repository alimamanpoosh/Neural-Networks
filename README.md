# CI_P2 (Neural Networks)

## Project Description

This project consists of three parts: "MLP from scratch", "NAS problem", and "Self-Organizing Map (SOM) from scratch". Each part serves a different purpose and is briefly described below:

### Part 1: MLP from scratch
In this part, a Multi-Layer Perceptron (MLP) is implemented from scratch using Python and NumPy. The MLP is trained on the CIFAR-10 dataset to classify images into one of the ten classes. The implementation includes forward and backward propagation, activation functions (sigmoid, tanh, and ReLU), and the Adam optimizer for parameter updates. The MLP is trained using the Adam optimizer, and the training loss is plotted against the number of epochs. Finally, the accuracy of the trained MLP on the training data is calculated and displayed.

### Part 2: NAS problem
In this part, a Neural Architecture Search (NAS) problem is formulated. The goal is to optimize the architecture of a neural network for feature extraction. The NAS problem is represented as a genetic algorithm, where chromosomes represent different configurations of neural network architectures. The fitness of each chromosome is evaluated based on the accuracy of the neural network on a given task. The genetic algorithm runs for a specified number of generations, and the best architecture found is displayed.

### Part 3: Self-Organizing Map (SOM) from scratch
In this part, we will implement a Self-Organizing Map (SOM) to cluster and visualize the CIFAR-10 dataset. SOM is an unsupervised learning algorithm that can be used for dimensionality reduction and clustering tasks.

