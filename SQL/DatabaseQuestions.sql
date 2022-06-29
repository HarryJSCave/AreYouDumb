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
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('What colour is grass?', 'Yellow', 'Green', 'Red', 'Blue', 'Green', 'Science');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('Who is often called the father of the computer?', 'Charles Babbage', 'Alan Turing', 'Leonardo da Vinci', 'Tim Berners-Lee', 'Charles Babbage', 'Science');
INSERT INTO questions(QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('Who discovered penicillin?', 'Thomas Edison', 'Alexander Fleming', 'Florence Nightingale', 'Christian Barnard', 'Alexander Fleming', 'Science');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES ("What's the body's largest organ?", 'Heart', 'Brain', 'Skin', 'Liver', 'Skin', 'Science');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES ('What is the planet closest to the sun?', 'Venus', 'Mercury', 'Mars', 'Saturn', 'Mercury', 'Science');

/*--Entertainment questions*/
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES("What is Hawkeye's real name?", 'Clint Barton', 'Tony Stark', 'Bruce Wayne', 'Oliver Queen', 'Clint Barton', 'Entertainment');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category) 
VALUES("What was Superman's birth name?", 'Christopher Nolan', 'Clark Kent', 'Zeus', 'Kal-El', 'Kal-El', 'Entertainment');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('What does DC stand for?', 'Discover Characters', 'Detective Comics', 'Deadly Comics', "Don't Care", 'Detective Comics', 'Entertainment');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES ('Who was the most streamed female artist of 2019?', 'Ariana Grande', 'Rihanna', 'Billie Eilish', 'Taylor Swift', 'Billie Eilish', 'Entertainment');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES ('Who had the best-selling album of 2020?', 'BTS', 'Billie Eilish', 'The Weeknd', 'Harry Styles', 'BTS', 'Entertainment');

/*--Sports questions*/
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('How many soccer players should each team have on the field at the start of the match?', '11', '12', '10', '9', '11', 'Sports');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('Who is the youngest winner of a Formula 1 World Championship?', 'Lewis Hamilton', 'Kimi Raikkonen', 'Sebastian Vettel', 'Michael Schumacher', 'Sebastian Vettel', 'Sports');
INSERT INTO questions(QuestionText, A1, A2, A3, A4, CA, Category)
VALUES("Which boxer was known as 'The Greatest' and 'The People's Champion'?", 'Bruce Lee', 'Mike Tyson', 'David Haye', 'Muhammad Ali', 'Muhammad Ali', 'Sports');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES ('What nationality was Ayrton Senna?', 'French', 'Portuguese', 'German', 'Brazilian', 'Brazilian', 'Sports');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES ('As of 2022, how many times has Roger Federer won at Wimbledone?', '6', '7', '8', '9', '8', 'Sports');


/*--Geography questions*/
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('Which two countries share the longest international border?', 'Canada/USA', 'China/Mongolia', 'Russia/Kazakhstan', 'China/India', 'Canada/USA', 'Geography');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('What is the capital city of New Zealand?', 'Christchurch', 'Wellington', 'Auckland', 'Tauranga', 'Wellington', 'Geography');
INSERT INTO questions(QuestionText, A1, A2, A3, A4, CA, Category)
VALUES("What is the world's longest river?", 'The Amazon', 'The Congo River', 'The Nile', 'The Yangtze River', 'The Nile', 'Geography');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES ('What is the smallest US state?', 'Hawaii', 'Rhode Island', 'Connecticut', 'Maryland', 'Rhode Island', 'Geography');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES ('Where will you find the Mariana Trench?', 'Pacific Ocean', 'Atlantic Ocean', 'North Sea ', 'Dead Sea', 'Pacific Ocean', 'Geography');


/*--History questions*/
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('What year did WW1 start?', '1918', '1914', '1911', '1908', '1914', 'History');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('What was the last dynasty of China?', 'Ming', 'Tang', 'Qing', 'Qin', 'Qing', 'History');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('Which famous battle took place on 18th June 1815?', 'Waterloo', 'Agincourt', 'Trafalgar', 'Turnbridge', 'Waterloo', 'History');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES ('What year was the Great Fire of London?', '1649', '1672', '1655', '1666', '1666', 'History');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES ('What year was the Wall Street Crash?', '1926', '1927', '1929', '1928', '1929', 'History');

/*--Art & Literature questions*/
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('Who wrote "Old Man and The Sea"?', 'J.R.R. Tolkien', 'George Orwell', 'Ernest Hemingway', 'Charles Dickens', 'Ernest Hemingway', 'Art');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('Who wrote The Merchant of Venice?', 'Jane Austen', 'William Shakespeare', 'Paul Allen', 'John Steinbeck', 'William Shakespeare', 'Art');
INSERT INTO questions (QuestionText, A1, A2, A3, A4, CA, Category)
VALUES('Claude Monet is most known for his paintings of what?', 'People', 'Sunflowers', 'Landscapes', 'Water lilies', 'Water lilies', 'Art);
