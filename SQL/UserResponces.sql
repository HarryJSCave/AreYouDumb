
CREATE TABLE user_responses(
	UserID TEXT NOT NULL,
    QuestionID TEXT NOT NULL,
	Answer TEXT NOT NULL,
    TimeTaken TIME NOT NULL,
	DateTaken DATE NOT NULL,
    Correct bit NOT NULL
);