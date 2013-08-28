TerrainGenerator
================

A terrain generation experiment using seed growing

Run using this command
	
	python runner.py

These are the optional command line arguments

usage: runner.py [-h] [-width WIDTH] [-height HEIGHT]
                 [-growth-threshold GROWTH_THRESHOLD] [-decay-rate DECAY]
                 [-number-of-seeds NUM_SEEDS] [-filename FILENAME]

A small program to generate simple terrains using seed growing

optional arguments:
  -h, --help            show this help message and exit
  -width WIDTH, -w WIDTH
  -height HEIGHT, -he HEIGHT
  -growth-threshold GROWTH_THRESHOLD, -g GROWTH_THRESHOLD
  -decay-rate DECAY, -d DECAY
  -number-of-seeds NUM_SEEDS, -n NUM_SEEDS
  -filename FILENAME, -f FILENAME
  
On OSX I use this command
	
	python runner.py && open map.png

Sample generated maps:

![sample generated map](map.png)
![sample generated map](small_islands.png)