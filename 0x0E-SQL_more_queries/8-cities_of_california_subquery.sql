-- list all the cities of california that can be found in database hbtn_0d_usa
SELECT id, name FROM cities WHERE id in (
	SELECT id FROM states WHERE name = 'California'
) ORDER BY name;
