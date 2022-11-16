.mode column
SELECT COUNT(DISTINCT Name) AS "Nombre d'appareil" FROM Probe;
SELECT Name AS "DEVICE",COUNT(Name) AS "CMPT" FROM Probe GROUP BY "DEVICE" ORDER BY "CMPT" DESC LIMIT 20;
SELECT date("Date") AS "jour", COUNT(date("Date")) AS "CMPT" FROM Probe GROUP BY "jour" ORDER BY "CMPT" DESC;
 