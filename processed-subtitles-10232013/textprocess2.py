"""
Author: Francisco Enrique Vicente Castro
Correspondence: fevgcastro@gmail.com
Description:
(Part 2) Python module for formatting text input file for individual lexicon sources (one per lm file);
Words are arranged alphabetically
Last modified: 18 October 2013
"""

import re

# File monitor numbers
start_number = 1
end_number = 42
end_number += 1 # For adjusting limit in range

# Directory names
source_dir = "OUTPUT-LM/"
dest_dir = "OUTPUT-LEX/"

"""--------------------------------------------------"""

for i in range( start_number, end_number ) :

    #---------------------------------------------------

    # File name to open
    filename = source_dir + "sub" + str( i ) + "-lm.txt"

    # Read file (Change according to source encoding)
    input_file = open( filename , "r" )
    #input_file = open( filename , encoding="utf-8" )

    # Split file into a list
    lines = input_file.read().split()

    # Close file
    input_file.close()

    #---------------------------------------------------

    # Set to store unique words
    ref = set()
    for word in lines :
        if ( word not in ref ) :
            ref.add( word )

    final_set = []
    for item in ref :
        final_set.append(item)

    final_set.sort()
    #---------------------------------------------------
    
    # File name for output
    filename = dest_dir + "sub" + str( i ) + "-lex.txt"

    # Write data
    output_file = open( filename, "w" )
    for item in final_set :
        output_file.write( item + "\n" )

    # Close output file
    output_file.close()

    #---------------------------------------------------
    