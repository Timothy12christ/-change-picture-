# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:17:10 2020

@author: ASUS
"""
x=int(input())
from PIL import Image#從套件中載入模組
FISH=Image.open('C:/Users/ASUS/Desktop/草包.jpg')#建立一個較FISH的變數，並輸入其路徑
FISH=FISH.convert('L')#修改模式，convert轉檔成L
FISH.show()
print(FISH.size)#尺寸 
print(FISH.mode)#模式
print(FISH.format)#格式'               
widthA,heightA,=FISH.size
width2A=int(widthA/2)
height2A=int(heightA/2)
newarea=FISH.resize((width2A, height2A))
#newarea_rotate = newarea_rotate(90)
newarea.show()
bigfish= newarea
bigfish_rotate= bigfish.rotate(x)#rotate角度
bigfish_rotate.show()

