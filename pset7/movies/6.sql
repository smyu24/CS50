select avg(rating) from ratings
join movies on ratings.movie_id = movies.id
WHERE year = 2012;