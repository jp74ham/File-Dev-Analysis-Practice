#finds all projects with the same name and combines them into one entry in the dictionary
#dictionary of filename, orig release date, latesst release date, orig size, latest size

import openpyxl
import datetime

files = {}

workbook = openpyxl.Workbook()
worksheet = workbook.active

worksheet.append(["File Name", "Original Release Date", "Latest Release Date", "Original Release Size", "Latest Release Size"])
workbook.save(filename = 'A1.xlsx')

def getUniqueFileName(fileVersions, nameNum):
    if (nameNum + 1) == (fileVersions.__len__()-1):
        uniqueName = ""
        for i in range (0,nameNum):
            uniqueName += fileVersions[i] + "-"
        uniqueName += fileVersions[nameNum]
        return uniqueName
    else:
        return getUniqueFileName(fileVersions, nameNum+1)

with open('../../SE-A1.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        parts = line.split()
        fileName = parts[0].replace(".tar.gz", "")
        date = parts[1]
        size = parts[2]
        fileVersions = fileName.split("-") #file , version
        if fileVersions.__len__() > 2: #if there is a second name in the file name
            uniqueName = getUniqueFileName(fileVersions, 0)
            if uniqueName in files: #if the file name is already in the dictionary
                if date < files[uniqueName]['earliest']['date']:
                    files[uniqueName]['earliest'] = {'date': date, 'size': size}
                if date > files[uniqueName]['latest']['date']:
                    files[uniqueName]['latest'] = {'date': date, 'size': size}
            else: #if file name not in dictionary
                files[uniqueName] = {'earliest': {'date': date, 'size': size}, 'latest': {'date': date, 'size': size}} #record the date and size
        
        else: #if just one name and version
            if fileVersions[0] in files: #if the file name is already in the dictionary
                if date < files[fileVersions[0]]['earliest']['date']:
                    files[fileVersions[0]]['earliest'] = {'date': date, 'size': size}
                if date > files[fileVersions[0]]['latest']['date']:
                    files[fileVersions[0]]['latest'] = {'date': date, 'size': size}
            else: #if file name not in dictionary
                files[fileVersions[0]] = {'earliest': {'date': date, 'size': size}, 'latest': {'date': date, 'size': size}} #record the date and size
                
                
                
for file in files:
    #print(file, files[file]['earliest']['date'], files[file]['latest']['date'], files[file]['earliest']['size'], files[file]['latest']['size'])
    worksheet.append([file, files[file]['earliest']['date'], files[file]['latest']['date'], files[file]['earliest']['size'], files[file]['latest']['size']])
workbook.save(filename = 'A1.xlsx')

