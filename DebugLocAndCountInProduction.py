import os
import re
import csv

assertCountDict = dict()


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        elif entry.find(".py") > 0:
            allFiles.append(fullPath)
    return allFiles


a = getListOfFiles('numpy-production/numpy')


for b in a:
    print(b)