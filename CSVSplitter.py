'''
Created on Jul 18, 2011

@author: encima
'''
import sys, csv


class CSVSplitter:
    '''
    classdocs
    '''
    def __init__(self, dir):
        my_file = open(dir, "rb")
        image = []
        for line in my_file:
            l = [i.strip() for i in line.split('~')]
            image.append(l)
        for index, img in enumerate(image):
            file = image[index][0].replace("\"", "") + ".csv"
            writer = csv.writer(open(file, "a"), delimiter='~', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(img)
        
csvsplit = CSVSplitter(sys.argv[1])