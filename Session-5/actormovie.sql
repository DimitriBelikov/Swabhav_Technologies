USE actormovie

CREATE TABLE actor(
	actor_id INT NOT NULL,
	actor_fname VARCHAR(20) NOT NULL,
	actor_lname VARCHAR(20) NOT NULL,
	PRIMARY KEY(actor_id)
);

CREATE TABLE movie(
	movie_id INT NOT NULL,
	movie_name VARCHAR(50) NOT NULL,
	release_date INT NOT NULL,
	PRIMARY KEY(movie_id)
);

CREATE TABLE movieactor(
	actor_id INT NOT NULL,
	movie_id INT NOT NULL,
	PRIMARY KEY(actor_id, movie_id),
	FOREIGN KEY (actor_id) REFERENCES actor(actor_id),
	FOREIGN KEY (movie_id) REFERENCES movie(movie_id)
);

INSERT INTO actor (actor_id, actor_fname, actor_lname) 
VALUES (001, 'Akshay', 'Kumar'),
		(002,'Saif Ali', 'Khan'),
		(003, 'Hritik', 'Roshan'),
		(004, 'Salman', 'Khan');

INSERT INTO movie (movie_id, movie_name, release_date)
VALUES (001, 'HouseFull 4', 2019),
		(002, 'Mujhse Shaadi Karoge', 2004),
		(003, 'Race 2', 2013),
		(004, 'Krish 2', 2013),
		(005, 'Hum Saath Saath Hai', 1999);
		
INSERT INTO movieactor (actor_id, movie_id)
VALUES (001, 001),
		(001,002),
		(002, 003),
		(002, 005),
		(003, 004),
		(004, 002),
		(004, 005);
		
SELECT actor.actor_fname, actor.actor_lname, movie.movie_name, movie.release_date
FROM actor
JOIN movieactor ON actor.actor_id = movieactor.actor_id
JOIN movie ON movie.movie_id = movieactor.movie_id
