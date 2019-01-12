#!/bin/bash

DIR_IMAGES=/home/pi/dev/learningpython/pictures/debug_pictures

INDIR_ANALYZER=$DIR_IMAGES
OUTDIR_ANALYZER=/home/pi/dev/learningpython/pictures/debug_pictures-new

python3 ./deer_detection2.py images $DIR_IMAGES

python3 ./deer_detection2.py analyze $INDIR_ANALYZER $OUTDIR_ANALYZER

