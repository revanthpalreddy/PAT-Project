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


def getTestFiles(path):
    testFiles = list()
    files = getListOfFiles(path)
    for forEachFile in files:
        index = forEachFile.rfind('/')
        fileName = forEachFile[index + 1:]
        if fileName.startswith("test"):
            testFiles.append(forEachFile)
    return testFiles


def skipLines(position, linesForSkipLines):
    numberOfLinesToBeSkippedForFromStatement = 0
    for j in range(position, len(linesForSkipLines)):
        if linesForSkipLines[j].find(")") > 0:
            numberOfLinesToBeSkippedForFromStatement += 1
            break
        else:
            numberOfLinesToBeSkippedForFromStatement += 1
    return numberOfLinesToBeSkippedForFromStatement


def getAssertLocAndCountForAFile(filePath):
    file = open(filePath, 'r')
    location = list()
    assertCount = 0
    assertDict = dict()
    debugDict = dict()
    lines = file.readlines()
    i = 0
    while i < len(lines):
        # Skip From Statement
        if re.search("^from", lines[i]) and lines[i].find("(") > 0:
            numberOfLinesToBeSkipped = skipLines(i + 1, lines)
            i = i + numberOfLinesToBeSkipped
        # Search Assert using Regex
        if re.search("^assert", lines[i]) or re.search("^\\s+assert", lines[i]):
            assertCount += 1
            location.append(i + 1)
        i += 1
    assertDict['assertCountAndLoc'] = [assertCount, location]
    assertCountDict[filePath] = assertDict


def getAssertLocAndCountForAllFiles():
    allFilesPath = getTestFiles(dirName)
    for eachFilepath in allFilesPath:
        getAssertLocAndCountForAFile(eachFilepath)


def writeToCSV():
    header = ['Relative Path', 'Module', 'File Name', 'Assert Location (Line Number)', 'Assert Count']
    with open('data/AssertLocAndCountInProduction.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for key, value in assertCountDict.items():
            module = re.findall("^[A-Za-z-]+\/[a-z]+\/([a-z_0-9]+)", key)
            fileName = key[key.rfind("/") + 1:]
            loactionList = value['assertCountAndLoc'][1]
            loactionInStrFormat = ','.join(str(e) for e in loactionList)
            if not (module[0].startswith("_")):
                writer.writerow([key, module[0], fileName, loactionInStrFormat, value['assertCountAndLoc'][0]])


dirName = 'numpy-production/numpy'

getAssertLocAndCountForAllFiles()
writeToCSV()
