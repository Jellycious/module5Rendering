class Sphere:

    # coordinates has to be tuple of (x, y, z)
    # slices is subdivisions of longitude
    # stacks is subdivision of latitude
    def __init__(self, radius, slices, stacks, coordinates, colour):
        self.radius = radius
        self.slices = slices
        self.stacks = stacks
        self.colour = colour
        if len(coordinates) == 3:
            self.coordinates = coordinates
        else:
            raise Exception("sphere takes a tuple in form (x, y, z)")


    # returns coordinates as tuple
    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        if len(coordinates) == 3:
            self.coordinates = coordinates
        else:
            raise Exception("set_coordinates takes argument as tuple in form (x, y, z)")

    def get_colour(self):
        return self.colour

    def get_radius(self):
        return self.radius

    def get_slices(self):
        return self.slices

    def get_stacks(self):
        return self.stacks

    # takes a tuple that has translate matrix in the form of (x-translate, y-translate, z-translate)
    def translate(self, translate_matrix):
        self.coordinates = (self.coordinates[0] + translate_matrix[0], self.coordinates[1] + translate_matrix[1],
                            self.coordinates[2] + translate_matrix[2])

