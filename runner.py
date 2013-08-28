import argparse
from terrainGenerator import TerrainGenerator

def main():
	parser = argparse.ArgumentParser(description="A small program to generate simple terrains using seed growing")

	parser.add_argument("-width", "-w", default=500, type=int, dest="width", help="The width of the generated image - default is 500")
	parser.add_argument("-height", "-he", default=500, type=int, dest="height", help="The height of the generated image - default is 500")
	parser.add_argument("-growth-threshold", "-g", default=0.9, type=float, dest="growth_threshold", help="The growth threshold above which a seed stops growing - default is 0.9")
	parser.add_argument("-decay-rate", "-d", default=0.01, type=float, dest="decay", help="The rate at which the growth threshold decreases - default is 0.01")
	parser.add_argument("-number-of-seeds", "-n", default=10, type=int, dest="num_seeds", help="The number of seeds to grow land from - default is 10")
	parser.add_argument("-filename", "-f", default="map.png", dest="filename", help="The output filename - default is map.png")

	arguments = vars(parser.parse_args())
	
	#width, height, growth threshold, decay rate, number of seeds
	tg = TerrainGenerator(arguments['width'], arguments['height'], arguments['growth_threshold'], arguments['decay'], arguments['num_seeds'], arguments['filename'])
	tg.generateTerrain()
	
if __name__ == '__main__':
	main()