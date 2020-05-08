import cx_Oracle

username = 'ralexeich'
password = '123456789'
database = 'localhost:1521/xe'

connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

print("Хронометраж Френка Оушена в чарті.\n")
query1 ="""
   select sum(track_duration) as all_playlist
from track
where artist= 'Frank Ocean'
"""
cursor.execute(query1)

for row in cursor:
    print(row)



print("Відсоток треків одного втконавця в чарті.\n")
query2 = """
SELECT artist , round((COUNT(artist))/ (SELECT COUNT(*) FROM track)*100, 2)  persent                                                                                                             
FROM track
GROUP BY artist
ORDER BY persent DESC, artist
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

