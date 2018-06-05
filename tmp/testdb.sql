DROP TABLE test.PRICE;
CREATE TABLE test.PRICE(ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY, NAME VARCHAR(200),CATEGORY1CODE INTEGER,CATEGORY2CODE INTEGER,CATEGORY3CODE INTEGER,SUB VARCHAR(100),PRICE INTEGER,ICON_IMG VARCHAR(500),UPDATE_TIME TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, INDEX(ID)) ENGINE=InnoDB;
ALTER TABLE test.PRICE AUTO_INCREMENT = 1;


DROP TABLE test.CATEGORY;
CREATE TABLE test.CATEGORY(ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY, CATEGORY1CODE INTEGER,CATEGORY1NAME VARCHAR(100), CATEGORY2CODE INTEGER,CATEGORY2NAME VARCHAR(100), CATEGORY3CODE INTEGER,CATEGORY3NAME VARCHAR(100),UPDATE_TIME TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, INDEX(ID)) ENGINE=InnoDB;
ALTER TABLE test.CATEGORY AUTO_INCREMENT = 1;
