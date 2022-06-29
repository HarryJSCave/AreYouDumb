DROP TABLE question_responses;

CREATE TABLE question_responses (
  QResponseID INT(11) NOT NULL AUTO_INCREMENT,
  ResponseText varchar(250) NOT NULL,
  Sentiment varchar(1) NOT NULL,
  PRIMARY KEY (QResponseID)
);


INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("You're not the stupidest person alive, but you better hope they don't die","N");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("You couldn't pour water out of a boot with the instructions on the heel.", "N");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("It's impossible to underestimate you.", "N");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("You have one braincell and it's bouncing around like a screensaver.", "N");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("Internet Explorer would have worked quicker than you.", "N");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("The wheel is spinning but the hamster's dead.", "N");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("At this point you can only impress me.", "N");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("Next time you get wrong there will be consequences", "N");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("You're doing amazing sweetie :)", "P");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("You only go that that right because you cheated!", "P");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("Yeah it's correct but you still can't live forever, weak human!", "P");
INSERT INTO question_responses (ResponseText, Sentiment) VALUES ("You are as smart as Fish with a really big brain", "P");