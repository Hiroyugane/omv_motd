#!/usr/bin/env python
# from configparser import ConfigParser
# Debug Info
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
#
import math
import subprocess
import os
import re
import socket
import urllib.request
from glob import glob
from configparser import ConfigParser
import calendar
import datetime

# read config
config = ConfigParser()
config.read('config.ini')
colors = config._sections['colors']


# Fluid Column-Layout code (doesnt make sense to put it here already since rows wouldn't be filled)
# takes the rows of info (name,value) and amount of columns and puts out balanced rows in Row-array-result
def column_display(rows, num_columns=2):
    columns = []
    column = []
    #add row to column 
    for row in rows:
        column.append(row)
        #if the column has the right amount so that rows are balanced -> put column to columns and clear
        if len(column) >= math.floor(float(len(rows))/num_columns):
            columns.append(column)
            column = []
    #put remaining column in columnlist
    if len(column) > 0: columns.append(column)
    column = 0

    # go through rowkeys and rowvalues and set lengths/padding 
    col_texts = []
    for column in columns:
        coltext = []
        #max length for keys is the longest row in the column
        max_keylen = max([len(row[0]) for row in column])
        for row in column:
            #fill with padding and finish off row with values
            padding = ' '*(max_keylen-len(row[0]))
            coltext.append("%s: %s%s" % (row[0], padding, row[1]))
        col_texts.append(coltext)

    result = ""
    # as many times as the length of a row (shouldnt that be for every row?)
    for i in range(len(col_texts[0])):
        line = ""
        #for all columntexts
        for j, coltext in enumerate(col_texts):
            #if iteration-number if small than length of columntext
            if i < len(coltext):
                #if it's not the first row
                if j > 0:
                    #maximum value-length = the highest from the list (containing the length of all the first rows in the column that's at the index of the 2nd iterable number down one ) 
                    #maximum value-length = the highest of (lengths of all 1st rows in the column that's at the index of the 2nd iterable number down one ) 
                    max_vallen = max([len(row[1]) for row in columns[j-1]])
                    #length of the value of row i in column j-1 
                    vallen = len(columns[j-1][i][1])
                    #prepend appropriate amount of tabstops
                    line += "\t"*max([1, int(math.floor(float(max_vallen-vallen)/4))])
                #put in value for row 
                line += coltext[i]
        #line is added to result
        result += line + "\n"
    #result is all rows in n*columns
    return result

# takes the width of XYZ and something uncentered? and returns a result
def center_by(width, uncentered):
    result = ""
    #lines is an array of the uncentered things 
    lines = uncentered.split("\n")
    #length is highest raw-length of rows in lines 
    length = max([smartlen(line) for line in lines])
    for line in lines:
        #put every line in results and prepend half of width minus highest length
        result += ' '*int((width-length)/2) + line + "\n"
    return result