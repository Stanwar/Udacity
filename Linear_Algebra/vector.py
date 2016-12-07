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
            return Vector(normal)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
    
    def dotProduct(self,v):
        ans = 0
        try:
            ans = [x*y for x, y in zip(self.coordinates, v.coordinates)]
            return sum(ans)
        except ZeroDivisionError:
            raise Exception('Cannot calculate dot product for zero vector')
    
    def angle(self, v, angType):
        v1 = v.normalize()
        v2 = self.normalize()
  
        angle_rad = math.acos(round(v1.dotProduct(v2),3))
        if angType == 'DEGREES':
            return angle_rad * (180./math.pi)
        else : 
            return angle_rad

    def isParallel(self, v):
        return (self.isZero() or 
                v.isZero() or 
                self.angle(v,'RADIANS') == 0)

    def isOrthogonal(self, v, tolerance = 1e-10):
        return abs(self.dotProduct(v)) < tolerance
    
    def isZero(self, tolerance= 1e-10):
        return self.magnitude() < tolerance

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

## Dot Product of the vectors
vector10 = Vector([7.887, 4.138])
vector11 = Vector([-8.802, 6.776])
print(vector11.dotProduct(vector10))
vector12 = Vector([-5.955,-4.904,-1.874])
vector13 = Vector([-4.496, -8.755, 7.103])
print(vector12.dotProduct(vector13))

## Cos angle between the vectors
vector14 = Vector([3.183, -7.627])
vector15 = Vector([-2.668, 5.319])
print(vector14.angle(vector15, 'RADIANS'))
vector16 = Vector([7.35,0.221,5.188])
vector17 = Vector([2.751,8.259,3.985])
print(vector16.angle(vector17, 'DEGREES'))

## Parallelism and Orthogonality
vector18 = Vector([-7.579, -7.88])
vector19 = Vector([22.737, 23.64])
print(vector18.isParallel(vector19))