import openpyxl
import os

workbook = openpyxl.Workbook()
worksheet = workbook.active

# worksheet.append(["File Name", "Original Release Date", "Latest Release Date", "Original Release Size", "Latest Release Size"])
# with open('../../A1-final.txt', 'r', encoding = 'utf-8') as readfile, open('../../A1-final_temp.txt', 'w', encoding = 'utf-8') as writefile:
#     for line in readfile:
#         parts = line.split("\t")
#         if parts[6] != "0":
#             writefile.write(line)

# os.remove('../../A1-final.txt')
# os.rename('../../A1-final_temp.txt', '../../A1-final.txt')

with open('../../A1-final.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        parts = line.split("\t")
        worksheet.append([parts[0], parts[1], parts[2], parts[3], parts[4], parts [5], parts[6], parts[7], parts[8]])
        
workbook.save("../../A1-final2.xlsx")