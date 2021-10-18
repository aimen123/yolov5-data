import os
import shutil

f = open("/home/numen/Desktop/yolox-data/VOC2007/ImageSets/Main/val.txt")             
lines = f.readlines()

f1 = open("/home/numen/Desktop/yolov5-data/val.txt",'r+') 


for line in lines:
    data = '/home/numen/Desktop/yolov5-data/images/' + line[:-1] + '.jpg' + '\n'
    f1.write(data)


f.close()
f1.close()

