CREATE TABLE `city` (
	`id` INT(255) NOT NULL AUTO_INCREMENT,
	`name` TEXT NOT NULL,
	`state` INT NOT NULL,
	`coordinates` POINT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `news` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`city_id` INT,
	`state_id` INT,
	`date` DATETIME NOT NULL,
	`title` VARCHAR(255) NOT NULL,
	`url` TEXT NOT NULL,
	`source_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `state` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `source` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL,
	`type` TEXT NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `city` ADD CONSTRAINT `city_fk0` FOREIGN KEY (`state`) REFERENCES `state`(`id`);

ALTER TABLE `news` ADD CONSTRAINT `news_fk0` FOREIGN KEY (`city_id`) REFERENCES `city`(`id`);

ALTER TABLE `news` ADD CONSTRAINT `news_fk1` FOREIGN KEY (`state_id`) REFERENCES `state`(`id`);

ALTER TABLE `news` ADD CONSTRAINT `news_fk2` FOREIGN KEY (`source_id`) REFERENCES `source`(`id`);


