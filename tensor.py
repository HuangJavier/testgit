import tensorflow as tf
import math
import numpy as np
import pandas as pd
import scipy as sp
import os
import tensorflow as tf

def main():
	#for i in range (10):
	#	print (i, end=' ')
	matrix1 = tf.constant([[3., 3.]])

	matrix2 = tf.constant([[2.],[2.]])

	product = tf.matmul(matrix1, matrix2)

	print (product)

	print ('\nYES')

if __name__ == '__main__':
	main()