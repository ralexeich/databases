import cx_Oracle

username = 'ralexeich'
password = '123456789'
database = 'localhost:1521/xe'

connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

print("Хронометраж артистів у чарті в чарті.\n")
query1 ="""
select distinct artist, track_duration
from track
"""
cursor.execute(query1)

for row in cursor:
    print(row)



print("Відсоток треків одного втконавця в чарті.\n")
query2 = """
select artist , round((count(artist))/ (select count(*) from track)*100, 2)  persent                                                                                                             
from track
group by artist
order by persent desc, artist
"""
cursor.execute(query2)

for row in cursor:
    print(row)



print("Динаміка залежності.Популярність від хронометражу.\n")
query3 = """
   select charts_place, max(popularity) as  popular
from charts
group by charts_place
order by charts_place
"""
cursor.execute(query3)



for row in cursor:
    print(row)


cursor.close()
connection.close()

