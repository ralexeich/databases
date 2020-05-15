import cx_Oracle
import re
import chart_studio
from plotly import graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dash

chart_studio.tools.set_credentials_file(username='ralexeich', api_key='c97HRRjX5X3Zb1j2SQW1')

def fileId_from_url(url):
    raw_fileId = re.findall("~[A-z.0-9]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

username = 'ralexeich'
password = '123456789'
database = 'localhost:1521/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

cursor.execute(  """
   select distinct artist, track_duration
from track
""" )

artist = []
track_duration = []


for row in cursor:
    print("artist:", row[0],"track_duration :",row[1])
    track_duration += [row[1]]
    artist += [row[0]]

data = [go.Bar(
             x=artist,
             y=track_duration 
      )]

layout = go.Layout(
    title = '',
    xaxis=dict(
        title='track_duration ',
        titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7d7d7d'
        )
    ),
    yaxis=dict(
        title='artist',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7d7d7d'
        )
    )
)

fig = go.Figure(data=data, layout=layout)

track_duration_artist = py.plot(fig, filename='duration -artist')

cursor.execute( """
   SELECT artist , round((COUNT(artist))/ (SELECT COUNT(*) FROM track)*100, 2)  persent                                                                                                             
FROM track
GROUP BY artist
ORDER BY persent DESC, artist
   """)
artist = []
percent = []

for row in cursor:
    artist.append(row[0])
    percent.append(row[1])

pie_data = go.Pie(
        labels=artist,
        values=percent,
        title="Вивести відсоток треків з однієї платформи у чарті."
    )
artist_percent = py.plot([pie_data], filename='artist-percent')


cursor.execute( """
   select charts_place, max(popularity) as  popular
from charts
group by charts_place
order by charts_place
""")

chart_place = []
popular = []

for row in cursor:
    print("chart_place", row[0], " popular: ", row[1])
    chart_place += [row[0]]
    popular += [row[1]]

chart_place_popular = go.Scatter(
    x=chart_place,
    y=popular,
    mode='lines+markers'
)
data = [chart_place_popular]
chart_place_popular_url = py.plot(data, filename='popular_chart_place')


my_dboard = dash.Dashboard()
track_duration_artist_id = fileId_from_url(track_duration_artist)
artist_percent_id = fileId_from_url(artist_percent)
chart_place_popular_id = fileId_from_url(chart_place_popular_url)

box_1= {
    'type': 'box',
    'boxType': 'plot',
    'fileId': track_duration_artist_id,
    'title': 'Запит 1 - Вивести загальний хронометраж артиста у плейлисті чарту.'
}
box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': artist_percent_id,
    'title': 'Запит 2 -  Вивести відсоток треків з однієї платформи у чарті.'

}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': chart_place_popular_id,
    'title': ' Вивести динаміку популярностей в залежності від місця в чарті.'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'right', 2)

py.dashboard_ops.upload(my_dboard, 'Billboard1')


cursor.close()
connection.close()


