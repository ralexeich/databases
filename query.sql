-- query1 
select sum(track_duration) as all_playlist
from track
where artist= 'Frank Ocean';



-- query2
select region_name, round((count(region_name))/(select count(*) from region)*100, 2) persent
from region
group by region_name
order by persent DESC , region_name;




-- query3
select charts_place, max(popularity) as  popular
from charts
group by charts_place
order by charts_place;
