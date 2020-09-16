#!/bin/bash
#Script that would tell you how many files is in you current directory
# Javian Williams 9/15/2020

files=`ls -l | wc -l`

echo You have $files files in your directory