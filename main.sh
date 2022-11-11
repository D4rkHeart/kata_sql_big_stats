#!/usr/bin/env sh
python3 ./DataBase/mainV1.py;
sqlite3 sensorRecord.db;
.timeout 2000
.mode column;
SELECT COUNT(DISTINCT Name) AS "Nombre d'appareil" FROM Probe;
SELECT Name AS "DEVICE",COUNT(Name) AS "CMPT" FROM Probe GROUP BY "DEVICE" ORDER BY "CMPT" DESC LIMIT 20;

