from xlrd import open_workbook
x_data1=[]
y_data1=[]
wb = open_workbook('phase_detector.xlsx')
for s in wb.sheets():
    print('Sheet:',s.name)
    for row in range(s.nrows):
        print('the row is:',row)
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(values)
        x_data1.append(values[0])
        y_data1.append(values[1])