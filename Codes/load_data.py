import xlrd
from partnership import Partners

def load(filename):
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    rows = sheet.nrows
    columns = sheet.ncols

    partners = []
    for i in range(1, rows):
        St = sheet.cell_value(i, 0)
        S = St.split(", ")
        for j in range(1, columns):
            S.append(sheet.cell_value(i, j))
        partners.append(Partners(S[0], S[1], S[2], S[3], S[4], S[5], S[6], S[7], S[8], S[9], S[10], S[11], S[12]))
    return partners

def get_batting_average_dictionary(filename):
    dictionary={}
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    rows = sheet.nrows

    for i in range(1, rows):
        St = sheet.cell_value(i, 0)
        S = St.split(" (")
        dictionary[S[0]]=sheet.cell_value(i,10)

    return dictionary