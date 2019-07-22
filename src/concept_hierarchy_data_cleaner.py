"""
author @22PoojaGaur

This file takes tesco provided concept hierarchy dataset and cleans it.

Input format -

num.[item-name]
{PATH=}[Item-path-separated-by-/]

Output format -

[item-name]
[item-path-separated-by-spaces]
"""

import sys

def main():
    file_name = sys.argv[1]
    out_file_name = sys.argv[2]
    line = ''

    try:
    	fin = open(file_name, 'r')
    except:
    	print ('Enter Correct File Name')
    	sys.exit()
    fout = open(out_file_name, 'w')

    is_item_line=1
    for line in fin.readlines():
    	if is_item_line:
    		it_name = line.split('.')[1].strip()
    		fout.write(it_name.replace(' ', '_') + '\n')
    		is_item_line = 0
    	else:
    		full_path = line.split('=')[1]
    		path_array= full_path.split('/')

    		for category in path_array:
    			fout.write(category.strip().replace(' ', '_') + ' ')

    		fout.write('\n\n')
    		is_item_line = 1

    fin.close()
    fout.close()

if __name__ == '__main__':
    main()
