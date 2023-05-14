from keras.datasets import cifar10
from classification_models.keras import Classifiers
import numpy as np

# uncomment this to download the weights of resnet34 if you don't have the .h5 file (85MB)
import urllib.request
url = 'https://github.com/qubvel/classification_models/releases/download/0.0.1/resnet34_imagenet_1000.h5'
urllib.request.urlretrieve(url, 'resnet34_imagenet_1000.h5')


# Get the CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()


# Load the pre-trained ResNet34 model
ResNet34, preprocess_input = Classifiers.get('resnet34')
x_train = preprocess_input(x_train)
x_test = preprocess_input(x_test)
model = ResNet34(input_shape=(32, 32, 3), weights='resnet34_imagenet_1000.h5')