DROP TABLE user_responses;
CREATE TABLE user_responses(
    ResponseID INT NOT NULL AUTO_INCREMENT, 
	UserID TEXT NOT NULL,
    QuestionID INT NOT NULL,
	Answer TEXT NOT NULL,
    TimeTaken FLOAT NOT NULL,
	DateTaken DATE NOT NULL,
    Correct bit NOT NULL,
    PRIMARY KEY (ResponseID),
    FOREIGN KEY (QuestionID) REFERENCES questions(QuestionID)
);