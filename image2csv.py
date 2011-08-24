import os, time, sys, csv, EXIF
from datetime import datetime

if len(sys.argv)!=3:
    print 'Usage: image2csv directory csvname'
    sys.exit(0)

class Image2Csv:
    def __init__(self, dir):
        writer = csv.writer(open(dir + "/" + sys.argv[2] + ".csv","w"), delimiter='~', quotechar='"', quoting=csv.QUOTE_ALL)
        self.sortJPEGs(dir, writer)

    @staticmethod
    def getFiles(dir):
        files = [s for s in os.listdir(dir)]
        files.sort(key=lambda s: os.path.getctime(os.path.join(dir, s)))
        return files
    
    @staticmethod
    def sortJPEGs(dir, writer):
        files = ImagePropPrinter.getFiles(dir)
        if files != None:
            startDate = datetime.strptime(time.ctime(os.path.getmtime(dir + "/" + files[0])), "%a %b %d %H:%M:%S %Y")
        for fileName in files:
            filePath = dir + "/" + fileName
            folders = filePath.split(os.sep)
            folders = filter(None, folders)
            if os.path.isdir(filePath) ==True:
                ImagePropPrinter.sortJPEGs(filePath, writer)
            elif "JPG" in fileName:
                fileSize = os.path.getsize(filePath)/1024
                fileCreation = datetime.strptime(time.ctime(os.path.getmtime(filePath)), "%a %b %d %H:%M:%S %Y")
                timeDiff = fileCreation - startDate
                diff = divmod(timeDiff.days * 86400 + timeDiff.seconds, 60)
                if diff[1] > 30:
                    ticks = diff[0] + 1
                else:
                    ticks = diff[0]
                cam = folders[4]
                writer.writerow([cam, fileCreation, filePath, fileSize, ticks])

        
imProp = Image2Csv(sys.argv[1])