#!/bin/bash

inputfilename=DPP4SubstrateHumanList.txt

# Create a dedicated diretory to store MEROPS retrive
DIRNAME=SubstrateMEROPSRecords
DIR=./$DIRNAME
if [ ! -d "$DIR" ] 
then mkdir $DIR
fi 

# Read substate MEROPS ids
cat $inputfilename | while read line
do
	# Debug
	# echo $line

	python SubMerops.py $line $DIRNAME
done
