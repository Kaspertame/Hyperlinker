import openpyxl
#open excel file (replace links.xlsx with correct file name)
wb = openpyxl.load_workbook('links.xlsx')
#add hyperlink to all cells in column A
for row in wb['Sheet1'].iter_rows(min_row=2, max_row=216, min_col=1, max_col=1):
    for cell in row:
        print(cell.value)
        query = str(cell.value)
        cleanquery = query.replace(' ', '-')
        cell.hyperlink = 'https://support.huntress.io/hc/en-us/articles/'+cleanquery
#save file (replace linktest.xlsx with file name you want to save)
wb.save('linktest.xlsx')