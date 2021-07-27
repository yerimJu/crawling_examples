import openpyxl

FILENAME = 'stats_104102.xlsx'
book = openpyxl.load_workbook(FILENAME)

sheet = book.active

for i in range(0,9):
    total = int(sheet[str(chr(i+66)) + '3'].value)
    seoul = int(sheet[str(chr(i+66)) + '4'].value)
    output = total - seoul
    print(f'Population except Seoul: {output}')

    sheet[str(chr(i+66)) + '21'] = output
    cell = sheet[str(chr(i+66)) + '21']

    cell.font = openpyxl.styles.Font(size=14, color='FF0000')
    cell.number_format = cell.number_format

FILENAME = 'population_result.xlsx'
book.save(FILENAME)
print('done.')
