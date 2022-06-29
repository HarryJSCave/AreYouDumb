DROP TABLE users;

CREATE TABLE users(
    GoogleID varchar (128) NULL,
    Username TEXT NOT NULL,
    PRIMARY KEY (GoogleID)
);

drop table leaderboard;
CREATE TABLE leaderboard
(
    EntryId INT NOT NULL AUTO_INCREMENT,
    UserID varchar (128) NULL,
    TotalScore INT NOT NULL,
	AverageTime FLOAT NOT NULL,
    TotalPlays INT NOT NULL,
    Category TEXT NOT NULL,
    PRIMARY KEY (EntryId),
    FOREIGN KEY (UserID) REFERENCES users(GoogleID)
    )