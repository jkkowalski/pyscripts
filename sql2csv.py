import csv
import cx_Oracle


conn = cx_Oracle.connect(user, pass, db, encoding='utf-8')

curr = conn.cursor()
curr.execute(query);


with open('out.csv', 'w') as csv_f:
    w = csv.writer(csv_f, delimiter=";", quotechar='"')
    w.writerow([i[0] for i in curr.description])
    w.writerows(curr)

csv_f.close()
conn.close()
