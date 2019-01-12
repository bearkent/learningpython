#!/bin/bash

DIR_IMAGES=/home/pi/dev/learningpython/pictures/debug_pictures

INDIR_ANALYZER=$DIR_IMAGES
OUTDIR_ANALYZER=/home/pi/dev/learningpython/pictures/debug_pictures-new

python3 ./deer_detection.py image $DIR_IMAGES

python3 ./deer_detection.py analyze $INDIR_ANALYZER $OUTDIR_ANALYZER

