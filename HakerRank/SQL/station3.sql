-- Query a list of CITY names from STATION for cities that have an even ID number. 
-- Print the results in any order, but exclude duplicates from the answer.

--  SELECT DISTINCT CITY FROM STATION WHERE MOD(ID,2) = 0;
-- SELECT CITY FROM STATION WHERE ID % 2 = 0 GROUP BY CITY;
select distinct(CITY) from STATION where ID % 2 = 0;