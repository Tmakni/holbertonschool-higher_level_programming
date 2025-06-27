-- List User
SELECT ts.title
        tg.name
FROM tv_shows       AS ts
LEFT JOIN tv_show_genres AS sg ON sg.show_id = ts.id
LEFT JOIN tv_genres     AS tg ON tg.id      = ts.id
ORDER BY ts.title ASC, tg.name ASC;
