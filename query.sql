-- query1 
select distinct artist, track_duration
from track;



-- query2
select artist , round((count(artist))/ (select count(*) from track)*100, 2)  persent                                                                                                             
from track
group by artist
order by persent desc, artist;




-- query3
select charts_place, max(popularity) as  popular
from charts
group by charts_place
order by charts_place;
