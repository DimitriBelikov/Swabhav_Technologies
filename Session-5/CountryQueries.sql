SELECT country.Name, city.Name, countrylanguage.`Language`
FROM country
JOIN city ON city.CountryCode = country.Code
JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
WHERE country.Name = 'India'


SELECT country.Code, country.Name, country.Population
FROM country
ORDER BY country.Population DESC
LIMIT 5