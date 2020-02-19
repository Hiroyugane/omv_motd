#!/usr/bin/env python
# from configparser import ConfigParser
import math
import subprocess
import os
import re
import socket
import urllib.request
from glob import glob
from configparser import ConfigParser

# read config
config = ConfigParser()
config.read('config.ini')
colors = config._sections['colors']



# colorize a string and reset color afterwards 
def colored(col, s):
    return colors[col] + s + colors['reset']

# divide bytes by 1024 and change suffix to Datasize "1GB is easier than 1024MB etc"
def humanise(byte_int):
    for x in ['bytes', 'KiB', 'MiB', 'GiB', 'TiB']:
        #if bigger than 1024, divide, go a size further, till under 1024
        if byte_int < 1024.0:
            #have a minimum of 3-digit-numbers incl. decimals
            if byte_int < 10:
                return "%1.2f%s" % (byte_int, x)
            else:
                return "%4.1f%s" % (byte_int, x)
        byte_int /= 1024.0

# smart length: check the length of the line as it'd be output
def smartlen(line):
    # replace tabs with 4 whitespaces
    line = line.replace("\t", ' '*4)
    #remove colorcodes
    for color in colors.keys():
        line = line.replace(colors[color], '')
    return len(line)

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

# is used to use commands easier. BASE DEF
def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True, stderr=subprocess.PIPE).decode('utf-8').strip()

# this definition return true if the service requested is running
# maybe add a function to search for services?
# why cant it use use_cmd()?
def service_active(service):
    cmd = '/bin/systemctl is-active %s' % service
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.communicate()
    if proc.returncode == 0:
        return True
    return False
