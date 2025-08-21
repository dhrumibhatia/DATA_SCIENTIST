-- Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
select c.name from CITY c where c.countrycode = 'JPN';