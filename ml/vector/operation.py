import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set()

"""depiction of vector"""
"""Plotting vector (4,5)"""
# plt.quiver(0,0,4,5,scale_units='xy',angles='xy',scale=1)
# plt.xlim(-8,8)
# plt.ylim(-8,8)
# plt.show()

""" function to plot multiple vector """
def multiple_vector(x:int,y:int,a:int,b:int):
    plt.quiver(0,0,x,y,scale_units='xy',angles='xy',scale=1,color='b')
    plt.quiver(0,0,a,b,scale_units='xy',angles='xy',scale=1,color='y')
    plt.xlim(-8,8)
    plt.ylim(-8,8)
    plt.show()

"""function to add two vectors"""
def add_vectors():
    vector_1 = np.asarray([0,0,1,4])
    vector_2= np.asarray([0,0,2,6])
    sum = vector_1+vector_2
    print(sum)
    return sum

"""function to multiply vector with scalar"""
def multiply_vector():
    vector_1 = np.asarray([0,0,2,3])
    scalar = 2
    result= scalar * vector_1
    print(result)
    return result

"""function to find dot product of two vectors"""
def dot_product():
    x = np.array([1,3])
    y= np.array([2,4])
    result = np.dot(x,y)
    print(result)

def cross_product():
    x = np.array([1,3])
    y = np.array([2,4])
    result= np.cross(x,y)
    print(result)


"""Projection of vector x on v """

def projection_vector():
    x = np.array([1,2])
    v = np.array([3,4])
    # magnitude of v
    magnitude_of_v = np.sqrt(sum(v**2))
    projection_of_x_on_v = (np.dot(x,v)/magnitude_of_v**2)*v
    print(projection_of_x_on_v)


if __name__=="__main__":
    # multiple_vector(3,4,1,6)
    # add_vectors()
    # multiply_vector()
    # dot_product()
    # cross_product()
    projection_vector()