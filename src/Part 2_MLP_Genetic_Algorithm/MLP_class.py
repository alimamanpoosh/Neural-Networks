import numpy as np
import matplotlib.pyplot as plt
Loss_train_adam = []
class MultiClassMLP:
    def __init__(self, input_dim, hidden_dims, output_dim, activation='relu', random_seed=42):
        self.input_dim = input_dim
        self.hidden_dims = hidden_dims
        self.output_dim = output_dim
        self.layers = []   # weights and biases for each layer
        self.num_layers = len(hidden_dims) + 1
        parameters = {}

        # Initialize weights and biases for each layer
        np.random.seed(random_seed)
        layer_dims = [input_dim] + hidden_dims + [output_dim]
        self.activations = [
            self._sigmoid if activation == 'sigmoid' else self._tanh if activation == 'tanh' else self._relu for i in
            range(self.num_layers)]
        for i in range(self.num_layers):
            fan_in = layer_dims[i]
            fan_out = layer_dims[i + 1]
            W = np.random.randn(fan_in, fan_out) / np.sqrt(fan_in)
            b = np.zeros((1, fan_out))
            
            self.layers.append({'W': W, 'b': b})
            
    def find_range_weight():
        max = 0
        min = np.inf
        for i in range(self.num_layers):
            if max < np.max(self.layers[i]['W']):
                max = np.max(self.layers[i]['W'])
            if min > np.min(self.layers[i]['W']):
                min = np.min(self.layers[i]['W'])
        return max, min
    

    def update_parameters(self):
        self.parameters = {}
        for counter, i in enumerate(self.layers):
            self.parameters.update({"W" + str(counter + 1): i["W"], "b" + str(counter + 1): i["b"]})

    def update_layers(self):
        for i in range(self.num_layers):
            self.layers[i]['W'] = self.parameters["W" + str(i + 1)]
            self.layers[i]['b'] = self.parameters["b" + str(i + 1)]

    def _softmax(self, X):
        exps = np.exp(X - np.max(X, axis=1, keepdims=True))
        return exps / np.sum(exps, axis=1, keepdims=True)


    def _tanh(self, X):
        return np.tanh(X)

    def _sigmoid(self, X):
        return 1 / (1 + np.exp(-X))

    def _relu(self, X):
        return np.maximum(0, X)

    def _forward(self, X):
        activations = [X]
        for i in range(self.num_layers):
            Z = np.dot(activations[-1], self.layers[i]['W']) + self.layers[i]['b']
            A = self.activations[i](Z)
            activations.append(A)
        probs = self._softmax(activations[-1])  # Using softmax activation function for output layer
        return activations, probs

    def _backward(self, X, y, activations, probs, learning_rate):
        grads = {}
        dL_dO = probs - y
        for i in reversed(range(self.num_layers)):
            if self.activations[i] == self._sigmoid:
                dA = dL_dO * activations[i + 1] * (1 - activations[i + 1])
            elif self.activations[i] == self._tanh:
                dA = dL_dO * (1 - activations[i + 1] ** 2)  # Derivative of tanh activation function
            elif self.activations[i] == self._relu:
                dA = dL_dO * np.where(activations[i + 1] > 0, 1, 0)  # Derivative of ReLU activation function
            else:
                raise ValueError("Invalid activation function")

            dZ = np.dot(dA, self.layers[i]['W'].T)
            dW = np.dot(activations[i].T, dA)
            db = np.sum(dA, axis=0, keepdims=True)
            grads.update({"dW" + str(i + 1): dW, "db" + str(i + 1): db})
            # self.layers[i]['W'] -= learning_rate * dW
            # self.layers[i]['b'] -= learning_rate * db

            dL_dO = dZ
        return grads

    def initialize_adam(self, parameters):
        L = len(parameters) // 2
        v = {}
        s = {}
        for l in range(L):
            v["dW" + str(l + 1)] = np.zeros(
                (parameters["W" + str(l + 1)].shape[0], parameters["W" + str(l + 1)].shape[1]))
            v["db" + str(l + 1)] = np.zeros(
                (parameters["b" + str(l + 1)].shape[0], parameters["b" + str(l + 1)].shape[1]))
            s["dW" + str(l + 1)] = np.zeros(
                (parameters["W" + str(l + 1)].shape[0], parameters["W" + str(l + 1)].shape[1]))
            s["db" + str(l + 1)] = np.zeros(
                (parameters["b" + str(l + 1)].shape[0], parameters["b" + str(l + 1)].shape[1]))
        return v, s

    def update_parameters_with_adam(self, parameters, grads, v, s, t, learning_rate=0.01, beta1=0.9, beta2=0.999,
                                    epsilon=1e-8):
        """
        Update parameters using Adam

        Arguments:
        parameters -- python dictionary containing your parameters:
                        parameters['W' + str(l)] = Wl
                        parameters['b' + str(l)] = bl
        grads -- python dictionary containing your gradients for each parameters:
                        grads['dW' + str(l)] = dWl
                        grads['db' + str(l)] = dbl
        v -- Adam variable, moving average of the first gradient, python dictionary
        s -- Adam variable, moving average of the squared gradient, python dictionary
        learning_rate -- the learning rate, scalar.
        beta1 -- Exponential decay hyperparameter for the first moment estimates
        beta2 -- Exponential decay hyperparameter for the second moment estimates
        epsilon -- hyperparameter preventing division by zero in Adam updates

        Returns:
        parameters -- python dictionary containing your updated parameters
        v -- Adam variable, moving average of the first gradient, python dictionary
        s -- Adam variable, moving average of the squared gradient, python dictionary
        """

        L = len(parameters) // 2  # number of layers in the neural networks
        v_corrected = {}  # Initializing first moment estimate, python dictionary
        s_corrected = {}  # Initializing second moment estimate, python dictionary

        # Perform Adam update on all parameters
        for l in range(L):
            # Moving average of the gradients. Inputs: "v, grads, beta1". Output: "v".
            ### START CODE HERE ### (approx. 2 lines)
            v["dW" + str(l + 1)] = beta1 * v["dW" + str(l + 1)] + (1 - beta1) * grads['dW' + str(l + 1)]
            v["db" + str(l + 1)] = beta1 * v["db" + str(l + 1)] + (1 - beta1) * grads['db' + str(l + 1)]
            ### END CODE HERE ###

            # Compute bias-corrected first moment estimate. Inputs: "v, beta1, t". Output: "v_corrected".
            ### START CODE HERE ### (approx. 2 lines)
            v_corrected["dW" + str(l + 1)] = v["dW" + str(l + 1)] / (1 - beta1 ** t)
            v_corrected["db" + str(l + 1)] = v["db" + str(l + 1)] / (1 - beta1 ** t)
            ### END CODE HERE ###

            # Moving average of the squared gradients. Inputs: "s, grads, beta2". Output: "s".
            ### START CODE HERE ### (approx. 2 lines)
            s["dW" + str(l + 1)] = beta2 * s["dW" + str(l + 1)] + (1 - beta2) * np.square(grads['dW' + str(l + 1)])
            s["db" + str(l + 1)] = beta2 * s["db" + str(l + 1)] + (1 - beta2) * np.square(grads['db' + str(l + 1)])
            ### END CODE HERE ###

            # Compute bias-corrected second raw moment estimate. Inputs: "s, beta2, t". Output: "s_corrected".
            ### START CODE HERE ### (approx. 2 lines)
            s_corrected["dW" + str(l + 1)] = s["dW" + str(l + 1)] / (1 - beta2 ** t)
            s_corrected["db" + str(l + 1)] = s["db" + str(l + 1)] / (1 - beta2 ** t)
            ### END CODE HERE ###

            # Update parameters. Inputs: "parameters, learning_rate, v_corrected, s_corrected, epsilon". Output: "parameters".
            ### START CODE HERE ### (approx. 2 lines)
            parameters["W" + str(l + 1)] = parameters["W" + str(l + 1)] - learning_rate * v_corrected[
                "dW" + str(l + 1)] / (np.sqrt(s_corrected["dW" + str(l + 1)]) + epsilon)
            parameters["b" + str(l + 1)] = parameters["b" + str(l + 1)] - learning_rate * v_corrected[
                "db" + str(l + 1)] / (np.sqrt(s_corrected["db" + str(l + 1)]) + epsilon)
            ### END CODE HERE ###

        return parameters, v, s

    def train(self, X_train, y_train, learning_rate=0.0007, mini_batch_size=64, beta=0.9,
              beta1=0.9, beta2=0.999, epsilon=1e-8, num_epochs=10000, print_cost=True):
        Y_train = np.eye(self.output_dim)[y_train]
        t = 0
        self.update_parameters()
        v, s = self.initialize_adam(self.parameters)
        for epoch in range(num_epochs):
            activations, probs = self._forward(X_train)
            grads = self._backward(X_train, Y_train, activations, probs, learning_rate)
            self.update_parameters()
            t = t + 1
            self.parameters, v, s = self.update_parameters_with_adam(self.parameters, grads, v, s,
                                                                t, learning_rate, beta1, beta2, epsilon)
            self.update_layers()
            loss = -np.sum(Y_train * np.log(probs)) / X_train.shape[0]
            if epoch % 10 == 0:
                Loss_train_adam.append(loss)
                print(f"Epoch {epoch}: Loss={loss:.4f}")

    def predict_proba(self, X):
        _, probs = self._forward(X)
        return probs

    def predict(self, X):
        probs = self.predict_proba(X)
        return np.argmax(probs, axis=1)


    
