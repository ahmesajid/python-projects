#!/bin/bash

DATE=$(date "+%Y-%m-%d_%H-%M-%S")
echo $DATE

FNAME="${DATE}-BKP"
echo "MAKING FOLDER $FNAME"

BKP_FOLDER="python-projects"

FOLDER="A:/python/projects"

cd $FOLDER
mkdir $FNAME
cp -r $BKP_FOLDER $FNAME 
