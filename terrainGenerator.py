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

        #Construct the map
        image = Image.new("RGB", (self.width, self.height), (0, 128, 255))

        #Get access to the pixel data
        self.map = image.load()

        for x in xrange(self.num_seeds + 1):
            #Determine the seed
            seed = int(random.random() * self.width * self.height)
            self._grow_seed(seed % self.width, seed / self.width,
                    self.growth_threshold)

        #Turn the map into a png
        image.save(self.filename)


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
    
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        pass

    def __setitem__(self, index, value):
        pass

class Point
            
        