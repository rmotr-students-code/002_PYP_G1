-- Countries
INSERT INTO country (id, name) VALUES (1, 'United States');
INSERT INTO country (id, name) VALUES (2, 'England');
INSERT INTO country (id, name) VALUES (3, 'Argentina');
INSERT INTO country (id, name) VALUES (4, 'Scotland');

-- Authors
INSERT INTO author (id, country_id, name) VALUES (1, 1, 'Edgar Allan Poe');
INSERT INTO author (id, country_id, name) VALUES (2, 1, 'Mark Twain');
INSERT INTO author (id, country_id, name) VALUES (3, 4, 'Arthur Conan Doyle');
INSERT INTO author (id, country_id, name) VALUES (4, 3, 'Jorge Luis Borges');

-- Books
INSERT INTO book (id, author_id, title ,isbn) VALUES (1, 1, 'The Raven', '978-3-16-148410-0');
INSERT INTO book (id, author_id, title ,isbn) VALUES (2, 2, 'The Adventures of Tom Sawyer', '9712-1232-12321-0');
INSERT INTO book (id, author_id, title ,isbn) VALUES (3, 4, 'Rmotr and Love', '000-3-99-123456-0');
INSERT INTO book (id, author_id, title ,isbn) VALUES (4, 1, 'The Tell-Tale Heart', '0030-3-93239-1256-0');
