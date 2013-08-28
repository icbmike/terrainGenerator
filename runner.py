from terrainGenerator import TerrainGenerator

def main():
	tg = TerrainGenerator(700, 500, 0.9, 0.005, 20)
	tg.generateTerrain()
	
if __name__ == '__main__':
	main()