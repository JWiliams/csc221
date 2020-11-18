#!/usr/bin/env python3 
''' Regex Search

Author: Javian Williams
'''
import argparse, os
from pathlib import Path

def regex_search(folder_path, regex):
    x = Path(folder_path)
    files = x.glob('*.txt')
    
    for file in files:
        fileObj = open(file)
        readFile = fileObj.readlines()
        for wordLine in readFile:
            if regex in wordLine:
                print (wordLine) 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='Folder to search for .txt files')
    parser.add_argument('regex', help='Regular expression to search for')

    args = parser.parse_args()

    regex_search(args.folder, args.regex)

if __name__=='__main__':
    main()

