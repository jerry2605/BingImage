#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:09:26 2020

@author: haopeng
"""

'''
how to run
# Assign execution permissions
1. chmod +x bingImage.py

#  # Run the script by using its filename
2. ./bingImage.py
'''

import urllib.request
from bs4 import BeautifulSoup
import wget
import os.path

#CN bing link, can access anywhere and only one(two ?) backgroup each day.
bingLink = 'https://cn.bing.com/?mkt=zh-CN'

savePath = '/Users/haopeng/Documents/BingBest/'

resolutionRatio = '1920x1080'


def downloadBingBg(BingLink, savePath):
    html = urllib.request.urlopen(bingLink).read()
    soup = BeautifulSoup(html, 'lxml')
    
    bgImageDiv = soup.find('div', attrs = {'id': 'bgImgProgLoad'})
    bgImageUrl = bgImageDiv['data-ultra-definition-src'].split('&')[0].replace('_UHD','')
    bgImageUrl = bgImageUrl.replace('.jpg', '_' + resolutionRatio +'.jpg')
    imageName = bgImageUrl.split('.',1)[1]
    bgImageUrl  = 'https://cn.bing.com' + bgImageUrl
    
    if os.path.isfile(savePath + imageName):
        print(imageName + ' is exist, skip downloading')
    else:
        filename = wget.download(bgImageUrl, savePath + imageName) # –output FILE|DIR output filename or directory
        print(filename + ' is downloaed to ' + savePath)


if __name__ == '__main__':
    downloadBingBg(bingLink, savePath)
