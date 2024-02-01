#created SE-A1.xlsx file and text.txt file in the same directory
#excel sheet contains name, date, size of all files

import openpyxl

workbook = openpyxl.Workbook()
worksheet = workbook.active

worksheet.append(["File Name", "Date Last Modified", "Latest Release Size"])

workbook.save(filename = 'SE-A1.xlsx')

with open('../../text.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        if ".tar.gz" in line and not ".tar.gz." in line: #only if the line contains .tar.gz and not .tar.gz.
            indexof_targz = line.index(".tar.gz")
            name = line[:indexof_targz+len('.tar.gz')].strip() #name is from the start of the line to the end of the .tar.gz
            restOfLine = line[indexof_targz+len('.tar.gz'):].strip()
            parts = restOfLine.split() 
            if len(parts) == 3:
                worksheet.append([name, parts[0], parts [2]])
            
            
workbook.save(filename = 'SE-A1.xlsx')
print("Excel file updated")