#!/bin/bash 
while read line;
do
	echo $line
	#echo "${array[@]}"
done < "$1"	
