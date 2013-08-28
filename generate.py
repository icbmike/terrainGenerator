import sys, random
from PIL import Image

def main():
	
	width = 1000
	height = 1000
	
	#Construct the map
	image = Image.new("RGB", (width, height), (0, 128, 255))
	
	#Get access to the pixel data
	pixels = image.load()

	for x in xrange(6):
		#Determine the seed
		seed = int(random.random() * width * height)
		grow_seed(seed / width, seed % width, pixels, width, height, 0.99, 0.001)

	#Turn the map into a png
	image.save('map.png')

def grow_seed(seed_x, seed_y, map, width, height, growth_threshold, decay):
	
	if random.random() > growth_threshold: 
		map[seed_x, seed_y] = (23, 115, 27)
		return
	elif map[seed_x, seed_y] == (23, 115, 26):
		return
	else:
		map[seed_x, seed_y] = (23, 115, 26)
		if seed_x != 0:
			grow_seed(seed_x - 1, seed_y, map, width, height,growth_threshold - decay, decay)

		if seed_x != width - 1:
			grow_seed(seed_x + 1, seed_y, map, width, height,growth_threshold - decay, decay)

		if seed_y != 0:
			grow_seed(seed_x, seed_y - 1, map, width, height,growth_threshold - decay, decay)

		if seed_y != height - 1:
			grow_seed(seed_x, seed_y + 1, map, width, height,growth_threshold - decay, decay)

if __name__ == '__main__':
	main()
