"""
Author: Francisco Enrique Vicente Castro
Correspondence: fevgcastro@gmail.com
Description:
(Part 1) Python module for formatting text input file for language model
Last modified: 22 October 2013
"""

import re

# File monitor numbers
start_number = 1
end_number = 42
end_number += 1 # For adjusting limit in range

# Directory names
source_dir = "TXT/"
dest_dir = "OUTPUT-LM/"

"""--------------------------------------------------"""

for i in range( start_number, end_number ) :

    #---------------------------------------------------

    # File name to open
    filename = source_dir + "sub" + str( i ) + ".txt"

    # Read file (Change according to source encoding)
    input_file = open( filename , "r" )
    #input_file = open( filename , encoding="utf-8" )

    # Split file into a list
    lines = input_file.read().split( '\n' )

    # Close file
    input_file.close()

    #---------------------------------------------------

    # Concatenate all lines together in one line
    build_string = ""
    for item in lines :
        build_string += ( item + " " )

    #---------------------------------------------------

    # Remove cases of <string>:
    build_string = re.sub( r'\w+:\s?', '', build_string )
    # Remove special characters
    build_string = re.sub( '--', '', build_string )
    build_string = re.sub( r'[",#;*^‘’“”&+♫]', '', build_string )
    # Remove cases of (tawanan)
    # Remove cases of (palakpakan)
    # Remove cases of [<string>] or (<string>)
    build_string = re.sub( r'\[.*?\]|\(.*?\)', '', build_string )

    # Removal of other special characters
    build_string = re.sub( r'[Â™«]', '', build_string )
    
    # Remove all sentence terminators
    new_lines1 = re.split( r'[.?!]+', build_string )

    #---------------------------------------------------

    # Remove unnecessary spaces
    new_lines2 = []
    for item in new_lines1 :
        temp = item.split( " " )

        buildup = ""
        for word in temp :
            if (word != "") :
                buildup += word + " "

        new_lines2.append( buildup )

    #---------------------------------------------------

    # Uppercase all letters
    for j in range( 0, len( new_lines2 ) ) :
        new_lines2[ j ] = new_lines2[ j ].upper()

    #---------------------------------------------------

    build_last = ""
    for item in new_lines2 :
        build_last += ( item + "\n" )

    # Last attempt at clearing non-standard symbols
    build_last = re.sub( r'[Â™«]', '\n', build_last )
    build_last = build_last.strip()
    build_last += "\n"

    #---------------------------------------------------

    # File name for output
    filename = dest_dir + "sub" + str( i ) + "-lm.txt"

    # Write data
    output_file = open( filename, "w" )
    #for item in new_lines2 :
    #    output_file.write( item + "\n" )
    output_file.write(build_last)

    # Close output file
    output_file.close()

    #---------------------------------------------------
    """"""