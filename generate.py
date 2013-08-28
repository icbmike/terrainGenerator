import sys, random


def main():
	
	#Determine the seed
	seedfactor = int(sys.argv[1]) % 1000000 if len(sys.argv) > 1 else len("My awesome seed")
	seed = random.random() * seedfactor
	
	#Construct the map with all water
	map = [(0, 128, 255) for x in xrange(1000 * 1000)]

	print len(map)

if __name__ == '__main__':
	main()