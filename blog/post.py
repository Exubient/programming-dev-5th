import csv

CSV_PATH = '/Users/hyunjoongkim/Downloads/post.txt'
reader= csv.reader(open(CSV_PATH, 'rt', encoding='cp949'), delimiter="|")

columns=next(reader)

ls =[]

for row in enumerate(reader):
      data = dict(zip(columns, row))
      print(data['우편번호'])
      ls.append(data['우편번호'])

