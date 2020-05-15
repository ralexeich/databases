-- query1 
   select distinct artist, track_duration
from track;



-- query2
SELECT artist , round((COUNT(artist))/ (SELECT COUNT(*) FROM track)*100, 2)  persent                                                                                                             
FROM track
GROUP BY artist
ORDER BY persent DESC, artist;




-- query3
select charts_place, max(popularity) as  popular
from charts
group by charts_place
order by charts_place;
