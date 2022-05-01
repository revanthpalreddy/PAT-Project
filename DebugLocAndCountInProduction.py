import os
import re
import csv

debugCountDict = dict()


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath) and entry != "tests":
            allFiles = allFiles + getListOfFiles(fullPath)
        elif not (fullPath.endswith("tests") or fullPath.endswith("pyi") or fullPath.endswith(
                "pyc") or fullPath.endswith(".DS_Store") or "/testing" in fullPath):
            allFiles.append(fullPath)
    return allFiles


def getDebugLocAndCountForAFile(filePath):
    file = open(filePath, 'r')
    location = list()
    debugCount = 0
    lines = file.readlines()
    i = 0
    while i < len(lines):
        if re.search("log\.debug", lines[i]) or re.search("#if .*DEBUG.*", lines[i]) \
                or re.search("#ifdef .*DEBUG.*", lines[i]) or re.search("DebugPrint.*;", lines[i]):
            debugCount += 1
            location.append(i + 1)
        i += 1
    debugCountDict[filePath] = [debugCount, location]


def getDebugLocAndCountForAllFiles():
    allFilesPath = getListOfFiles(dirName)
    for eachFilepath in allFilesPath:
        getDebugLocAndCountForAFile(eachFilepath)


def writeToCSV():
    header = ['Relative Path', 'File Name', 'Debug Location (Line Number)', 'Debug Count']
    with open('data/DebugLocAndCountInProduction.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for key, value in debugCountDict.items():
            fileName = key[key.rfind("/") + 1:]
            loactionList = value[1]
            loactionInStrFormat = ','.join(str(e) for e in loactionList)
            writer.writerow([key, fileName, loactionInStrFormat, value[0]])


dirName = 'numpy-git/numpy'
getDebugLocAndCountForAllFiles()
writeToCSV()