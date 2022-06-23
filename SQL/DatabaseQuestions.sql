/*--CREATE DATABASE DC2060;
*/
DROP TABLE questions;


CREATE TABLE questions(
	QuestionID INT NOT NULL AUTO_INCREMENT, 
	QuestionText TEXT NOT NULL,
	A1 TEXT NOT NULL,
	A2 TEXT NOT NULL,
	A3 TEXT NOT NULL,
	A4 TEXT NOT NULL,
	CA TEXT NOT NULL,
	Category TEXT NOT NULL,
	PRIMARY KEY (QuestionID)
);


/*--adding questions to table
--Science questions*/
INSERT INTO questions
VALUES(1,'What colour is grass?', 'Yellow', 'Green', 'Red', 'Blue', 'Green', 'Science');
INSERT INTO questions
VALUES(2,'Who is often called the father of the computer?', 'Charles Babbage', 'Alan Turing', 'Leonardo da Vinci', 'Tim Berners-Lee', 'Charles Babbage', 'Science');
INSERT INTO questions
VALUES(3,'Who discovered penicillin?', 'Thomas Edison', 'Alexander Fleming', 'Florence Nightingale', 'Christian Barnard', 'Alexander Fleming', 'Science');

/*--Entertainment questions*/
INSERT INTO questions
VALUES(4,"What is Hawkeye's real name?", 'Clint Barton', 'Tony Stark', 'Bruce Wayne', 'Oliver Queen', 'Clint Barton', 'Entertainment');
INSERT INTO questions
VALUES(5,"What was Superman's birth name?", 'Christopher Nolan', 'Clark Kent', 'Zeus', 'Kal-El', 'Kal-El', 'Entertainment');
INSERT INTO questions
VALUES(6,'What does DC stand for?', 'Discover Characters', 'Detective Comics', 'Deadly Comics', "Don't Care", 'Detective Comics', 'Entertainment');

/*--Sports questions*/
INSERT INTO questions
VALUES(7,'How many soccer players should each team have on the field at the start of the match?', '11', '12', '10', '9', '11', 'Sports');
INSERT INTO questions
VALUES(8,'Who is the youngest winner of a Formula 1 World Championship?', 'Lewis Hamilton', 'Kimi Raikkonen', 'Sebastian Vettel', 'Michael Schumacher', 'Sebastian Vettel', 'Sports');
INSERT INTO questions
VALUES(9,"Which boxer was known as 'The Greatest' and 'The People's Champion'?", 'Bruce Lee', 'Mike Tyson', 'David Haye', 'Muhammad Ali', 'Muhammad Ali', 'Sports');

/*--Geography questions*/
INSERT INTO questions
VALUES(10,'Which two countries share the longest international border?', 'Canada/USA', 'China/Mongolia', 'Russia/Kazakhstan', 'China/India', 'Canada/USA', 'Geography');
INSERT INTO questions
VALUES(11,'What is the capital city of New Zealand?', 'Christchurch', 'Wellington', 'Auckland', 'Tauranga', 'Wellington', 'Geography');
INSERT INTO questions
VALUES(12,"What is the world's longest river?", 'The Amazon', 'The Congo River', 'The Nile', 'The Yangtze River', 'The Nile', 'Geography');

/*--History questions*/
INSERT INTO questions
VALUES(13,'What year did WW1 start?', '1918', '1914', '1911', '1908', '1914', 'History');
INSERT INTO questions
VALUES(14,'What was the last dynasty of China?', 'Ming', 'Tang', 'Qing', 'Qin', 'Qing', 'History');
INSERT INTO questions
VALUES(15,'Which famous battle took place on 18th June 1815?', 'Waterloo', 'Agincourt', 'Trafalgar', 'Turnbridge', 'Waterloo', 'History');

/*--Art & Literature questions*/
INSERT INTO questions
VALUES(16,'Who wrote "Old Man and The Sea"?', 'J.R.R. Tolkien', 'George Orwell', 'Ernest Hemingway', 'Charles Dickens', 'Ernest Hemingway', 'Art & Literature');
INSERT INTO questions
VALUES(17,'Who wrote The Merchant of Venice?', 'Jane Austen', 'William Shakespeare', 'Paul Allen', 'John Steinbeck', 'William Shakespeare', 'Art & Literature');
INSERT INTO questions
VALUES(18,'Claude Monet is most known for his paintings of what?', 'People', 'Sunflowers', 'Landscapes', 'Water lilies', 'Water lilies', 'Art & Literature');
