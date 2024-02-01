#changes size units into kB

import openpyxl

workbook = openpyxl.Workbook()
worksheet = workbook.active

worksheet.append(["File Name", "Original Release Date", "Latest Release Date", "Original Release Size", "Latest Release Size"])
with open('../../A1.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        parts = line.split("\t")
        origSize = parts[3]
        latestSize = parts[4]
        if origSize[-1] == "M": #if the last character is M for Orig Size
            origSize = float(origSize[:-1]) * 1024 # convert and take out unit for easy graphing in excel
            origSize = str(origSize)
        if latestSize[-1] == "M": #^^ for Latest Size
            latestSize = float(latestSize[:-1]) * 1024
            latestSize = str(latestSize)
        if origSize[-1] == "K": #If last character is K for Orig Size
            origSize = float(origSize[:-1]) #take out unit for easy graphing in excel
            origSize = str(origSize)
        if latestSize[-1] == "K":#^^ for Latest Size
            latestSize = float(latestSize[:-1])
            latestSize = str(latestSize)
        worksheet.append([parts[0], parts[1], parts[2], origSize, latestSize]) #append to excel worksheet

workbook.save("A1-final.xlsx")
