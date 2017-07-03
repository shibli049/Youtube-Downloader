import pafy
import os

from os.path import expanduser


def mycb(total, recvd, ratio, rate, eta):
    if( (int)(ratio*1000)%10 == 0):
        print(recvd, "{:.2f}".format((ratio*100)) , "{:.2f}".format((rate/8))  , (int)(eta) )


url = input("your url: ")
video = pafy.new(url)
print(video.title)
#for s in video.streams:
#   print(s)


chosen1 = video.getbestaudio()
streams = video.streams
#streams = video.audiostreams
i = 0

for s in streams:
    print(i, " : ", s.extension, s.get_filesize())
    i += 1

chosenOption = input("chosse from above list[0,1,2,...etc]: ")
chosen1 = streams[int(chosenOption)]
# chosen1 = video.getbestaudio()
home_folder = input("full path with file name to save: ")
#title = input("file name:")
#expanduser("~")

if(home_folder == None):
	home_folder = os.getenv('dl')
print(home_folder)
#filePath = home_folder + "/" + title + "." + chosen1.extension
filePath = home_folder + "." + chosen1.extension
print("s: " , chosen1.get_filesize(), chosen1.extension, chosen1.url)
"""
print(filePath)
finalPath = best.download(filepath=filePath, quiet=True, callback=mycb)
print(finalPath)
#best.download(quiet=False)"""

try:
    import wget
    filename = wget.download(chosen1.url, out=filePath, bar=wget.bar_thermometer)
    print(filename)
except ImportError as e:
    print("Download failed: ", chosen1.url)
#wget.download(best.url, bar=wget.bar_thermometer)
