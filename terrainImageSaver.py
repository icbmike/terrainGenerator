from PIL import Image

class TerrainImageSaver(object):
    def __init__(self, filename):
        self.filename = filename

    #The method called by a TerrainGenerator, terrain is expected to be a Terrain object
    def save_image(self, terrain):
        #Construct the map
        image = Image.new("RGB", (terrain.width, terrain.height), terrain.default_color)

        map = image.load()

        for point in terrain.get_data():
            map[point.x, point.y] = point.color

        image.save(self.filename)


        
