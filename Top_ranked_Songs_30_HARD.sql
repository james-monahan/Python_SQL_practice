-- Find the top-ranked songs for the past 30 years.


select song_name
from billboard_top_100_year_end
WHERE year >= DATE_PART('year',NOW())-30
AND year_rank = 1
