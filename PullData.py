#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:45:44 2020
I've written it as a function so you can just import this and it returns the appropriate dataframe.

df = getData()

@author: benmacadam
"""
import os
import requests
import shutil
import pandas as pd

def getData():
    # Set up file path
        
    # create a directory that does yet exists
    dirName = "temp"
    dirName = os.path.join(
        os.getcwd(), dirName
    )
    if not os.path.exists(dirName):
       os.mkdir(dirName)


    # Uses os.path.join in case anyone is on windows
    zipName = "data.zip"
    zipPath = os.path.join(dirName, zipName) 
    
    dataURL = "https://www150.statcan.gc.ca/n1/tbl/csv/38100286-eng.zip"
    
    ## Get the zip file
    resp = requests.get(dataURL)
    zipFile = open(zipPath, "wb")
    zipFile.write(resp.content)
    zipFile.close()
    
    # unpack the data into tempdata
    shutil.unpack_archive(zipName, extract_dir=dirName)
    
    # this gets the data
    
    dataPath = os.path.join(dirName, "38100286.csv")
    frame = pd.read_csv(dataPath)
    
    # now delete the tempdata folder
    shutil.rmtree(dirName)
    return frame