"""
Walks through the directory tree starting from a specified root
directory and lists files in decreasing order of size.
You can specify as a command-line argument how many number of
files you want displayed. If argument is omitted, it displays 10.
Works only on windows for now.
"""

import os, sys
from operator import itemgetter

sizemap = {}
def walkThroughDirectoryTree(dirname):
   """ Walks through the directories recursively and returns a dict 
   of {file path:file size}"""
   try:
      for root,dirs,files in os.walk(dirname):
         if files:
            for filename in files:
               fullfilename = os.path.join(root,filename)
               sizemap[fullfilename] = os.path.getsize(fullfilename)
   except:
      raise
      print "Error processing directory: " + dirname
   return sizemap
	
def printdict(sorteddict, rows):
   """ Loops through the sorted filepath/filesize tuple and prints the number of entries required"""
   for k,v in sorteddict[:rows]:
      print str(k) + " has size " + str(v)
			
if __name__ == '__main__': 
   #Sort the sizemap dict returned by walkThroughDirectoryTree by values and feed it to printdict to print out the file sizes
   printdict(sorted(walkThroughDirectoryTree("c:\Dev").items(), key=itemgetter(1), reverse=True),
               int(sys.argv[1]) if len(sys.argv) > 1 else 10)