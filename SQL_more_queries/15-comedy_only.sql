-- List User
SELECT  ts.title
FROM    tv_shows        AS ts
JOIN    tv_show_genres  AS sg  ON sg.show_id  = ts.id
JOIN    tv_genres       AS tg  ON tg.id       = sg.genre_id
WHERE   tg.name = 'Comedy'
ORDER BY ts.title ASC;
