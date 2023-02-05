SELECT name, ROUND(price, 0)
FROM fake_apps;


SELECT ROUND(imdb_rating),
   COUNT(name)
FROM movies
GROUP BY 1
ORDER BY 1;

Here, the 1 refers to the first column in our SELECT statement, ROUND(imdb_rating).