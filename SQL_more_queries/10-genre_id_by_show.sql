-- List User
SELECT  s.title,
        g.genre_id
FROM    tv_shows         AS s
JOIN    tv_show_genres   AS g  ON g.show_id = s.id
ORDER BY s.title ASC, g.genre_id ASC;
