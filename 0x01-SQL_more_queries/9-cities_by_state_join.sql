-- joining cities and state
SELECT cities.id, cities.name, states.name FROM cities
FROM cities
JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;