import sys
import os
text = 'anek.txt' #file name (test in .txt file)
with open(text, encoding='utf-8') as f, open("outfile.txt","w", encoding='utf-8') as outfile:
    for line in f:
        if not line.isspace():
            sys.stdout.write(line)
            outfile.write(line)
os.remove(text) #delete original file
os.rename('outfile.txt', text) #take input file name and rename output file