'''
JMJPFU
26-Feb-2020
THis is the script for the GAN lab
Lord bless this attempt of yours
'''
# Import the required library functions
from configparser import ConfigParser
import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import tensorflow as tf
from tensorflow.keras.layers import Input
from tensorflow.keras.initializers import RandomNormal
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Reshape, Dense, Dropout, Flatten
from tensorflow.keras.layers import LeakyReLU,BatchNormalization
from tensorflow.keras.layers import Conv2D, UpSampling2D,Conv2DTranspose
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.optimizers import Adam

# Getting the details of the arguments
ap = argparse.ArgumentParser()
ap.add_argument('--configfile',required=True,help='This is the path to the configuration files')
args = ap.parse_args()