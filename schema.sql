CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT UNIQUE, password TEXT);

CREATE TABLE babies (id SERIAL PRIMARY KEY, name TEXT UNIQUE, user_id INTEGER REFERENCES users);

CREATE TABLE breastfeeding (id SERIAL PRIMARY KEY, baby_id INTEGER REFERENCES babies, date DATE, time TIMESTAMP, duration TIME);

CREATE TABLE formula (id SERIAL PRIMARY KEY, baby_id INTEGER REFERENCES babies, date DATE, time TIMESTAMP, amount_ml INTEGER);

CREATE TABLE solid (id SERIAL PRIMARY KEY, baby_id INTEGER REFERENCES babies, date DATE, time TIMESTAMP, amount_gr INTEGER, food_id INTEGER REFERENCES food);

CREATE TABLE food (id SERIAL PRIMARY KEY, name TEXT);

CREATE TABLE diapers (id SERIAL PRIMARY KEY, baby_id INTEGER REFERENCES babies, date DATE, time TIMESTAMP, diaper_content_id INTEGER REFERENCES diaper_content);

CREATE TABLE diaper_content (id SERIAL PRIMARY KEY, name TEXT);

CREATE TABLE weight (id SERIAL PRIMARY KEY, baby_id INTEGER REFERENCES babies, date DATE, weight INTEGER);

CREATE TABLE messages (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users, baby_id INTEGER REFERENCES babies, date DATE, time TIMESTAMP, content TEXT);
