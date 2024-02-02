# Order of development:
1. A1.py 
    - webscraped the files ending in .tar.gz recursively from the website https://ftp.gnu.org/pub/gnu/ and saved it to text.txt

2. updateExcel.py
    - filtered through text.txt and put file names, dates, and sizes of only those ending in .tar.gz
    - put results into SE-A1.xlsx

converted SE-A1.xlsx file into SE-A1.txt

3. updateExcel2.py
    - searched through SE-A1.txt and consolidated all unique projs (proj names) and differentiated between Orig Release Date, Latest Release Date, Orig Release Size, and Latest Release Size
    - put results into A1.xlsx

converted A1.xlsx file into into A1.txt

4. A1-final.py
    - iterated through A1.txt and converted all sizes into kiloBytes, and removing unit char at the end of size
    - put results into A1-final.xlsx

converted A1-final.xlsx into A1-final.txt

5. A1-final2.py
    - looked through A1-final.txt and removed all files/lines only one release AKA with time interval (Latest Release Date - Original Release Date) == "0"
    - put results back into A1-final.txt
    - iterated through A1-final.txt again to finally put all files in A1-final2.xlsx
