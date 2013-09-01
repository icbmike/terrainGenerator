import random
from PIL import Image

class TerrainGenerator(object):

    def __init__(self, width, height, growth_threshold, decay, num_seeds, filename):
        self.width = width
        self.height = height
        self.growth_threshold = growth_threshold
        self.decay = decay
        self.num_seeds = num_seeds
        self.filename = filename
        self.recursion_counter = 0

    def get_recursion_depth(self):
        return self.recursion_counter

    def generate_terrain(self):

        #Get access to the pixel data
        self.map = Terrain()

        for x in xrange(self.num_seeds + 1):
            #Determine the seed
            seed = int(random.random() * self.width * self.height)
            self._grow_seed(seed % self.width, seed / self.width,
                    self.growth_threshold)


    def _grow_seed(self, seed_x, seed_y, growth_threshold):
        
        self.recursion_counter += 1
        
        if random.random() > growth_threshold:
        
            self.map[seed_x, seed_y] = (23, 115, 27)
            return
        
        elif self.map[seed_x, seed_y] == (23, 115, 26):
            return
        
        else:
            self.map[seed_x, seed_y] = (23, 115, 26)
            if seed_x != 0:
                self._grow_seed(seed_x - 1, seed_y, growth_threshold - self.decay)

            if seed_x != self.width - 1:
                self._grow_seed(seed_x + 1, seed_y, growth_threshold - self.decay)

            if seed_y != 0:
                self._grow_seed(seed_x, seed_y - 1, growth_threshold - self.decay)

            if seed_y != self.height - 1:
                self._grow_seed(seed_x, seed_y + 1, growth_threshold - self.decay)


class Terrain(object):
    
    def __init__(self, width, height, defaultColour=(0, 128, 255)):
        self.data = {}
        self.width = width
        self.height = height
        self.defaultColour = defaultColour

    def __getitem__(self, index):
        if index[0] < 0 or index[0] >= self.width or index[1] < 0 or index[1] >= self.height:
            raise IndexError()

        if index in self.data:
            return self.data[index]
        else:
            return self.defaultColour

    def __setitem__(self, index, value):
        if index[0] < 0 or index[0] >= self.width or index[1] < 0 or index[1] >= self.height:
            raise IndexError()
        self.data[index] = value

    def get_data(self):
        for key in self.data.keys():
            yield data[key];

class Point(object):
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
    
