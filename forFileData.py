import xlwt

book = xlwt.Workbook(encoding="utf-8")

sheet = book.add_sheet("SheetStars")

# открываем файл на чтение
C = open("C:/Users/Edik kek/Desktop/EX.txt","r")

i = 0
for s in C: # построчно читаем файл
    ss = s.split(",")
    j = 0
    for w in ss:
        if ss.index(w) == len(ss) - 1:
            q = w.split("\n")
            w = q[0]
        sheet.write(i, j, float(w))
        j += 1
    i += 1
    
book.save("C:/Users/Edik kek/Desktop/Stars.xls")
    
C.close()



