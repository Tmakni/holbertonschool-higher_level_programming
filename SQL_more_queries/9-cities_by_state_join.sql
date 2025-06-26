-- List User
SELECT  c.id,
        c.name,
        s.name AS state
FROM    cities  AS c
JOIN    states  AS s  ON s.id = c.state_id
ORDER BY c.id ASC;
