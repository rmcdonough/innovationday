#!/bin/bash

DIRS="python-app-1
python-app-2
python-app-3"

for DIR in $DIRS ; do
	echo BUILDING $DIR
	cd $DIR
	docker build -t $DIR .
	cd ..
	echo
	echo "*********"
	echo
done
