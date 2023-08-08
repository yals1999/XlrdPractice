import xlrd

path = r"C:/Users/Mallikarjun/PycharmProjects/FrameworkPractice/Framewrok/QTalkPswd.xlsx"
workBook_obj = xlrd.open_workbook(path)
worksheet_obj = workBook_obj.sheet_by_name("QTalk")

rows = worksheet_obj.get_rows()
header = next(rows)
d = {}
for row in rows:
    d = d[row[0].value] = (row[1].value, row[2].value)
    print(d)
