create table track(  
      track_name varchar(1000) not null PRIMARY KEY, 
      artist varchar(1000) not null, 
      track_duration integer not null 
);
create table region(
      region_name varchar(1000) not null PRIMARY KEY,
      full_spreading varchar(50) not null
);
     
create table charts(
      charts_place integer not null PRIMARY KEY,
      region_name varchar(1000) not null references region(region_name),
      track_name varchar(1000) not null references track(track_name),
      popularity integer not null
);


