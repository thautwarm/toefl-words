# -*- coding: utf-8 -*-

import os
import sys

# search file
def scan_files(directory, prefix=None, postfix=None):
    files_list = []

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list

# read files and parser
def read_files(directory_list):
    for file_name in directory_list:
        for line in open(file_name):
            if '##' not in line and '----' not in line and line.startswith('|'):
                line = line.replace(' ', '')
                if not line.startswith('||||'):
                    parser_line(line[1:])
        pass


# parser every line
def parser_line(line):
    index = line.find('|')
    global last_item
    if index > 0:
        word = line[:index]
        if not line.startswith('Word'):               
            word_item = [word, line[index:].replace('|',' ')]
            last_item = word_item
            word_dict.append(word_item)
    elif index == 0:
        last_item[1] += '\n' + line[index:].replace('|',' ')

# search element
def search_word():

    sys.stdout.write(">>>  ")
    sys.stdout.flush()    

    word = raw_input()
    word_list = []
    real_word = []

    if word == '':
        return
    elif word == 'fk':
        exit()
    elif word == 'up-':
        os.system('./update.sh')
        return
    elif word == 're-':
        # re - index 
        initial_search()
        return
    elif word == 'cl-':
        os.system('clear')
        return        

    for word_item in word_dict:
        if word_item[0] != None and word_item[0].startswith(word):
            word_list.append(word_item)
            if word_item[0] == word:
                real_word = word

    if len(real_word) != 0:
        print real_word
    else:
        print 'no real word'
    for item in word_list:
        # word
        print '\033[1;31m'
        print item[0]
        print '\033[0m'
        # expr
        print item[1].encode('utf-8')
        # block
        print '################################################'
    return

# initial and read file
def initial_search():
    word_dict = []
    last_item = []

    file_list = scan_files("./", None, ".md")[1:] # remove ReadMe.md

    read_files(file_list)
    pass

global word_dict

global last_item

word_dict = []
last_item = []

initial_search()

while True:
    search_word()
