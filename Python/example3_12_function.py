# Example of building a function

import math 

def cirArea(r):
    '''
    Calculating the surface area of a circle

    input parameter r: radius of the circle

    return value area: area of the circle
    '''
    area = math.pi * (r ** 2)

    return area

def rect_area(w,h=None):
    '''
    Calculating the surface area of the rectangle/square

    input parameter w : the width of the rectangle

    input parameter h : the height of the rectangle

    return output area: the area of the rectangle

    '''
    if h is None:
        return w * w
    else:
        return w * h 



#applying the function

print('Please insert a radius')

k = float(input())

type(k)

area = cirArea(k)

print('The area of the circle:',area)

print()

print('Please insert a width')

w = float(input())

print('Please insert a height')

h = float(input())

area_2 = rect_area(w,h)

print('The area of the rectangle:',area_2)

print()

