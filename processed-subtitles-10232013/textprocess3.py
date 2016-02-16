"""
Author: Francisco Enrique Vicente Castro
Correspondence: fevgcastro@gmail.com
Description:
(Part 4) Python module for formatting text input file for lexicon;
Output is a combined lexicon (unique words) from all statements from combined lm file;
Words are arranged alphabetically
Last modified: 22 October 2013
"""

import re

# Directory names
source_dir = "COMBINE-LM/"
dest_dir = "COMBINE-LEX/"

"""--------------------------------------------------"""

#---------------------------------------------------

# File name to open
filename = source_dir + "combine-lm.txt"

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
filename = dest_dir + "combine-lex.txt"

# Write data
output_file = open( filename, "w" )
for item in final_set :
    output_file.write( item + "\n" )

# Close output file
output_file.close()

#---------------------------------------------------