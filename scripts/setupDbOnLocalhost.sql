-- ######################################################################################## --
-- README                                                                                   --
-- ######################################################################################## --
-- Following script does:                                                                   --
--1. DB erstellen: `pythonTest`                                                             --
--2. User erstellen: `python`, PWD: `python`                                                --
--3. User Rechte zuweisen                                                                   --
--4. Tabelle `user` erstellen. Spalten:                                                     --
--      user_id (PK, AI)                                                                    --
--      name (varchar(255))                                                                 --
--      firstname (varchar(255))                                                            --
--      password (varchar(255))                                                             --
--      class (varchar(255))                                                                --
-- 5. Beispieldaten werden eingefügt                                                        --
-- ######################################################################################## --
-- HOW TO                                                                                   --
-- Execute the following script after being logged in as admin on a MySql-Server            --
-- ######################################################################################## --

CREATE DATABASE `pythonTest` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'python'@'localhost' IDENTIFIED BY '***';GRANT USAGE ON *.* TO 'python'@'localhost' IDENTIFIED BY '***' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON `pythonTest`.* TO 'python'@'localhost';
CREATE TABLE `pythonTest`.`user` ( `user_id` INT NOT NULL AUTO_INCREMENT COMMENT 'Id of the created user' , `name` VARCHAR(255) NOT NULL COMMENT 'name of the user' , `notes` TEXT NULL COMMENT 'notes concerning the user' , PRIMARY KEY (`user_id`)) ENGINE = InnoDB;
ALTER TABLE `pythonTest`.`user` ADD `firstname` VARCHAR(255) NOT NULL COMMENT 'firstname of the user' AFTER `name`, ADD `password` VARCHAR(255) NOT NULL COMMENT 'password of the user' AFTER `firstname`, ADD `class` VARCHAR(255) NOT NULL COMMENT 'class the user belongs to' AFTER `password`;
INSERT INTO `pythonTest`.`user` (`user_id`, `name`, `firstname`, `password`, `class`) VALUES (NULL, 'Mustermann', 'Max', '1234', 'IT4a');
INSERT INTO `pythonTest`.`user` (`user_id`, `name`, `firstname`, `password`, `class`) VALUES (NULL, 'Ute', 'Mustermann', '1234', 'IT4b');