#!/bin/bash

cd /home/pi/photos

ip addr | grep inet

python3 -m http.server
