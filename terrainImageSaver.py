from PIL import Image

class TerrainImageSaver(object):
    def __init__(self, filename):
        self.filename = filename

    #The method called by a TerrainGenerator, terrain is expected to be a Terrain object
    def saveImage(self, terrain):
        #Construct the map
        image = Image.new("RGB", (terrain.width, terrain.height), terrain.defaultColor)

        map = image.load()

        for point in terrain.data:
            map[point.x, point.y] = point.color

        image.save(self.filename)
        
