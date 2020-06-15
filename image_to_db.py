# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:47:25 2020

@author: chimochimo
"""

import numpy as np
from PIL import Image
import os, glob, random

photo_size = 75
x = []
y = []

def glob_images(path, label, max_photo):
    files = glob.glob(path + "/*.jpg")
    random.shuffle(files)
    for i, f in enumerate(files):
        if i >= max_photo: break
        
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((photo_size, photo_size))
        data = np.asarray(img)
        data = data / 256
        data = data.reshape(photo_size, photo_size, 3)
        x.append(data)
        y.append(label)

def make_dataset(max_photo, outfile):
    global x
    global y
    x = []
    y = []
    
    glob_images("./sakura-ok",0,max_photo)
    glob_images("./sunflower-ok",1,max_photo)
    glob_images("./rose-ok", 2, max_photo)
    x = np.array(x, dtype=np.float32)
    np.savez(outfile,x=x,y=y)
    print("saved:" + outfile)
    
make_dataset(100, "photo-min.npz")
make_dataset(300, "photo.npz")
        
        