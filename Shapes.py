class Object:
    def __init__(self, coordinates, colour, direction_matrix):
        if len(coordinates) == 3:
            self.coordinates = coordinates
        else:
            raise Exception("Object takes coordinates argument as tuple in form (x, y, z)")

        if len(coordinates) == 3:
            self.direction_matrix = direction_matrix
        else:
            raise Exception("Object takes direction argument as tuple in form (x, y, z)")

        self.colour = colour

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        if len(coordinates) == 3:
            self.coordinates = coordinates
        else:
            raise Exception("set_coordinates takes argument as tuple in form (x, y, z)")

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def translate(self, translate_matrix):
        self.coordinates = (self.coordinates[0] + translate_matrix[0], self.coordinates[1] + translate_matrix[1],
                            self.coordinates[2] + translate_matrix[2])


class Sphere(Object):

    # coordinates has to be tuple of (x, y, z)
    # slices is subdivisions of longitude
    # stacks is subdivision of latitude
    def __init__(self, radius, slices, stacks, coordinates, colour, direction_matrix):
        self.radius = radius
        self.slices = slices
        self.stacks = stacks
        Object.__init__(self, coordinates, colour, direction_matrix)

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_slices(self):
        return self.slices

    def get_stacks(self):
        return self.stacks

