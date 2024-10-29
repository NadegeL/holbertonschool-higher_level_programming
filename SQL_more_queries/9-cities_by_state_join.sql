--  lists all cities contained in the database hbtn_0d_usa

SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

/* 
JOIN states ON cities.state_id = states.id :
Cette ligne relie la table cities à la table states.
Elle dit : "Pour chaque ligne dans cities, trouve la ligne correspondante dans states où l'id de states correspond au state_id de cities
/*