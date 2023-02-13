-- hahaha
SELECT title FROM tv_show_genres INNER JOIN tv_shows 
ON tv_show_genres.show_id = tv_shows.id JOIN tv_genres 
ON genre_id = tv_genres.id
WHERE name = "Comedy" ORDER BY title ASC;