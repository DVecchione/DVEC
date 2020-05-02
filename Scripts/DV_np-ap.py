#Dylan Vecchione OCEAN 506 Numpy and Argparse Assignment

import numpy as np
import sys, os
import pickle


#Making arrays using varying techniques
Array1=np.array(np.linspace(0,1000,100).reshape((2,5,10)))
Array2=Array1*3.46
print("Array 1:\n", Array1)
print("\n\nArray 2:\n", Array2)
Array3=np.array(np.arange(50)).reshape((5,10))
print("\n\nArray 3:\n", Array3)
Array4=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]).reshape(4,5)
print("\n\nArray 4:\n", Array4)

#Applying Five Methods:

print("\n\nMethod 1, Shape of Array 1: \n",np.shape(Array1))
print("\nMethod 2, Sum of Array 2: \n",Array2.sum())
print("\nMethod 3, Flattening Array 3: \n",Array3.flatten())
print("\nMethod 4, Max of Array 4: \n",Array4.max())
print("\nMethod 5, Concatenate A4 and A4: \n", np.concatenate((Array4,Array4), axis=1))

# local imports
import my_module as mymod
from importlib import reload
reload(mymod)

# make sure the output directory exists
this_dir = os.path.abspath('.').split('/')[-1]
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../../' + this_parent + '_output/'
print('\n\nCreating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)

#Saving Array2 as a Pickel File
out_fn = out_dir + 'pickled_array.p'
pickle.dump(Array2, open(out_fn, 'wb')) # 'wb' is for write binary

# read the array back in
b = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary
print('\nThe shape of the loaded object is', b.shape)

#Argparse Command Line
import argparse

parser = argparse.ArgumentParser()
# Input the intended name of your output list as a string
#with tag -n
parser.add_argument('-n', '--List_name', default='My List', type=str)

#Input the range of numbers in the output list starting
#from 0 as an integer with tag -r
parser.add_argument('-r', '--range', default=10, type=int)

args=parser.parse_args()

#Prints your list title, followed by the array of length r
Array=np.array(np.arange(args.range))
print('\n\n'+args.List_name +' is:')
print(Array)
