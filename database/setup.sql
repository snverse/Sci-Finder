CREATE TABLE User (
	name		VARCHAR(99),
	password	CHAR(32),
	email		VARCHAR(150) UNIQUE,
	location 	VARCHAR(255),
	uLevel 		TINYINT UNSIGNED,
	ORCID 		INT,
	uid 		INT UNSIGNED PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE Tag (
	topic 		INT UNSIGNED,
	technique 	INT UNSIGNED,
	uid 		INT UNSIGNED PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE Lab (
	name		VARCHAR(255),
	uid		INT UNSIGNED PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE Page (
	research	MEDIUMTEXT,
	about		MEDIUMTEXT,
	user		INT UNSIGNED PRIMARY KEY,
	FOREIGN KEY (user) REFERENCES User (uid)
);

CREATE TABLE Dataset (
	id_pot		VARCHAR(255),
	link		VARCHAR(255),
	uid		INT UNSIGNED PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE Pub (
	doi		VARCHAR(255),
	title		VARCHAR(255),
	link		VARCHAR(255),
	uid		INT UNSIGNED PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE Tag_Width (
	user		INT UNSIGNED,
	tag		INT UNSIGNED,
	FOREIGN KEY (user) REFERENCES User (uid),
	FOREIGN KEY (tag) REFERENCES Tag (uid)
);

CREATE TABLE Lab_Team (
    	lab         	INT UNSIGNED,
    	user        	INT UNSIGNED,
    FOREIGN KEY (lab) REFERENCES Lab (uid),
    FOREIGN KEY (user) REFERENCES User (uid)
);

CREATE TABLE PI (
	pub		INT UNSIGNED,
	user		INT UNSIGNED,
	FOREIGN KEY (pub) REFERENCES Pub (uid),
	FOREIGN KEY (user) REFERENCES User (uid)
);

CREATE TABLE Uses_Technique (
	pub		INT UNSIGNED,
	technique	INT UNSIGNED,
	FOREIGN KEY (pub) REFERENCES Pub (uid),
	FOREIGN KEY (technique) REFERENCES Tag (uid)
);

CREATE TABLE Uses_Data (
	pub		INT UNSIGNED,
	dataset		INT UNSIGNED,
	FOREIGN KEY (pub) REFERENCES Pub (uid),
	FOREIGN KEY (dataset) REFERENCES Dataset (uid)
);

CREATE TABLE Pub_Author (
	pub         	INT UNSIGNED,
	user        	INT UNSIGNED,
	FOREIGN KEY (pub) REFERENCES Pub (uid),
	FOREIGN KEY (user) REFERENCES User (uid)
);

CREATE TABLE Produced_By (
	pub         	INT UNSIGNED,
	lab         	INT UNSIGNED,
	FOREIGN KEY (pub) REFERENCES Pub (uid),
	FOREIGN KEY (lab) REFERENCES Lab (uid)
);
