import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = coordinates
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be non empty')
        except TypeError:
            raise TypeError('The coordinates must be non iterable ')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self,v):
        return self.coordinates == v.coordinates

    def addition(self,v):
        ans = []
        for indx in range(0,len(v.coordinates)):
            ans.append(self.coordinates[indx] + v.coordinates[indx])
        return ans

    def substraction(self,v):
        ans = []
        for indx in range(0,len(v.coordinates)):
            ans.append(self.coordinates[indx] - v.coordinates[indx])
        return ans

    def scalar(self,mul):
        ans = []
        for indx in range(0,len(self.coordinates)):
            ans.append(mul*self.coordinates[indx])
        return ans
    
    def magnitude(self):
        ret = 0
        ret  = [x**2 for x in self.coordinates]
        ret = math.sqrt(sum(ret))
        return ret

    def normalize(self):
        try : 
            mag = self.magnitude()
            normal = self.scalar(1/mag)
            return normal
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

## Addition 
vector1 = Vector([8.218, -9.341])
vector2 = Vector([-1.129, 2.111])
print(vector1.addition(vector2))

## Substract
vector3 = Vector([7.119, 8.215])
vector4 = Vector([-8.223, 0.878])
print(vector3.substraction(vector4))

## Scalar Multiply
vector5 = Vector([1.671, -1.012, -0.318])
print(vector5.scalar(7.41))

## Magnitude
vector6 = Vector([-0.221, 7.437])
print(vector6.magnitude())
vector7 = Vector([8.813, -1.331, -6.247])
print(vector7.magnitude())

## Normalize
vector8 = Vector([5.581, -2.136])
print(vector8.normalize())
vector9 = Vector([1.996, 3.108, -4.554])
print(vector9.normalize())