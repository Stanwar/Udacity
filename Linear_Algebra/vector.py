class Vector(object):
    def init(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be non empty')
        except TypeError:
            raise TypeError('The coordinates must be non iterable ')

    def str(self):
        return 'Vector: {}'.format(self.coordinates)

    def eq(self,v):
        return self.coordinates == v.coordinates
