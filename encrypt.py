# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:52:33 2018

@author: Zebo
"""

fo = open("img.jpg" , "rb")

image = fo.read()

fo.close()

image = bytearray(image)

key = 48

for index , value in enumerate(image):
    image[index] = value^key
    
fo = open("enc.jpg" , "wb")

fo.write(image)

fo.close()