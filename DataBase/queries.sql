SELECT
  Name,
  COUNT(Name) AS `count` 
FROM Probe
GROUP BY Name
ORDER BY `count` DESC
LIMIT 20;
