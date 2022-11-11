SELECT COUNT(DISTINCT Name) AS "Nombre d'appareil" FROM Probe;

SELECT Name,COUNT(Name) AS "Nombre de réccurence"
FROM Probe
GROUP BY Name
ORDER BY "Nombre de réccurence" DESC
LIMIT 20;

