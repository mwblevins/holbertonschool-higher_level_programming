-- shows all
SELECT title, name FROM tv_shows LEFT OUTER JOIN tv_show_genres 
ON tv_shows.id = tv_show_genres.show_id LEFT OUTER JOIN tv_genres 
ON genre_id = tv_genres.id ORDER BY title, name ASC;