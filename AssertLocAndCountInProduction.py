import os
import re
import csv

assertCountDictInProd = dict()


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles =  list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath) and entry != "tests":
            allFiles = allFiles + getListOfFiles(fullPath)
        elif not (fullPath.endswith("tests") or fullPath.endswith("pyi") or fullPath.endswith(
                "pyc") or fullPath.endswith(".DS_Store") or "/testing" in fullPath):
            allFiles.append(fullPath)
    return allFiles


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
    lines = file.readlines()
    listOfLoc = list()
    assertCount = 0
    i = 0
    while i < len(lines):
        # Skip From Statement
        if re.search("^from", lines[i]) and lines[i].find("(") > 0:
            numberOfLinesToBeSkipped = skipLines(i + 1, lines)
            i = i + numberOfLinesToBeSkipped
        # Search Assert using Regex
        if (re.search("^assert", lines[i]) and lines[i].find("=") < 0) or re.search("^\\s+assert", lines[i]):
            assertCount += 1
            listOfLoc.append(i + 1)
        i += 1
    assertCountDictInProd[filePath] = [assertCount, listOfLoc]


def getAssertLocAndCountForAllFiles():
    dirName = "numpy-git/numpy"
    allFilesPath = getListOfFiles(dirName)
    for eachFilepath in allFilesPath:
        getAssertLocAndCountForAFile(eachFilepath)
    return assertCountDictInProd


def writeToCSV():
    header = ['Relative Path', 'File Name', 'Assert Location (Line Number)', 'Assert Count']
    with open('data/AssertLocAndCountInProduction.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for key, value in assertCountDictInProd.items():
            fileName = key[key.rfind("/") + 1:]
            loactionList = value[1]
            loactionInStrFormat = ','.join(str(e) for e in loactionList)
            writer.writerow([key, fileName, loactionInStrFormat, value[0]])
