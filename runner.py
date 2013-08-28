from terrainGenerator import TerrainGenerator

def main():
	#width, height, growth threshold, decay rate, number of seeds
	tg = TerrainGenerator(700, 500, 0.9, 0.001, 10) 
	tg.generateTerrain()
	
if __name__ == '__main__':
	main()