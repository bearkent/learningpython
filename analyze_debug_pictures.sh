#!/bin/bash

INDIR_ANALYZER=/home/pi/dev/learningpython/pictures/debug_pictures
OUTDIR_ANALYZER=/home/pi/dev/learningpython/pictures/debug_pictures-new


python3 ./deer_detection2.py analyze $INDIR_ANALYZER $OUTDIR_ANALYZER 
