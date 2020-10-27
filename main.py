import sys
import os, glob
import random
from PIL import Image, ImageDraw

import triangle as t
from genetic import GeneticAlgorithm

def main():

    '''Main function for the Genetic Algorithm program.

    This function will take in 3 or 4 arguements from the command line and a new 
    GeneticAlgorithm object will be created based on said arguements.

    GeneticAlgorithm(`image`, `population size`, `reproduction method`)
    `crossover_rate`: rate at which crossover occurs (i.e. 0.7 => 70% crossover chance)

    -- The `images` folder will be wiped each time the program is executed. --
    '''
    file_name = sys.argv[1]
    population = int(sys.argv[2])
    mode = sys.argv[3].lower()

    g = GeneticAlgorithm(file_name, population, mode)
    
    # If the mode is sexual, implement crossover rate
    if mode == 'sexual':

        crossover_rate = float(sys.argv[4])

        if crossover_rate > 1 or population <= 1:

            exit('\n-- Something is wrong with your arguements. See README file. --\n')

    # Cleans the images folder from the program's previous run
    files = glob.glob('images/*')

    for file in files:

        os.remove(file)

    # Creates a number of "blank" pictures based on the population size
    gen0 = [(Image.new('RGB', size=(256, 256))) for _ in range(g.population)]
    
    # Drawing triangles on the initial population
    # List format: [image, triangles within image]
    gen0 = t.init_draw(gen0)

    # Selecting the best parent(s) from the list of triangles
    g.selection(gen0) 

    if g.mode == 'sexual':
        
        new_gen = g.crossover()

        while not g.selection(new_gen):

            if crossover_rate > random.random():

                new_gen = g.crossover()
            
            else:

                new_gen = g.asexual()

    else:

        new_gen = g.asexual()

        while not g.selection(new_gen):

            new_gen = g.asexual()
        

if __name__ == '__main__':

    main()