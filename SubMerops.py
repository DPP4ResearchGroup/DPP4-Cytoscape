import urllib2
from bs4 import BeautifulSoup
import sys
import os.path 

if __name__ == "__main__":
	SubID = str (sys.argv[1]) 
	DIR = str (sys.argv[2])

	web_handle = "http://merops.sanger.ac.uk/cgi-bin/merops.cgi?id=substrate;action=" + SubID
	# Debug
	print web_handle 

	html = urllib2.urlopen (web_handle)

	soup = BeautifulSoup (html.read(),"lxml")

	# Debug
	# print soup

	table = soup.find ("table")

	# The first tr contains the field names.
	headings = [th.get_text() for th in table.find("tr").find_all("th")]

	# Debug
	# print headings

	datasets = []
	for row in table.find_all("tr")[1:]:
	    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
	    datasets.append(dataset)

	# Write Final Records
	write_handle = SubID + ".merops.txt"
	currentpath = os.path.dirname(os.path.realpath(__file__))
	save_path =  DIR
	writefilefullpath = os.path.join (currentpath, save_path, write_handle)
	wfile = open (writefilefullpath,"w")
    		
	wfile.write("source\ttarget\n")
	peptidases = []
	for dataset in datasets:
		for index, item in dataset:
			if ((index == "Peptidase") & (item.lower() != "unknown peptidase")) :
				peptidases.append(item)
	
	peptidases = set(peptidases)
	for peptidase in peptidases:
		wfile.write (SubID+"\t"+str(peptidase)+"\n")

	wfile.close()
