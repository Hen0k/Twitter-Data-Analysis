CREATE TABLE IF NOT EXISTS `tweets_information` 
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `created_at` TEXT NOT NULL,
    `source` VARCHAR(200) NOT NULL,
    `original_text` VARCHAR(300) DEFAULT NULL,
    `polarity` FLOAT DEFAULT NULL,
    `subjectivity` FLOAT DEFAULT NULL,
    `language` TEXT DEFAULT NULL,
    `favorite_count` INT DEFAULT NULL,
    `retweet_count` INT DEFAULT NULL,
    `original_author` TEXT DEFAULT NULL,
    `screen_count` INT NOT NULL,
    `followers_count` INT DEFAULT NULL,
    `friends_count` INT DEFAULT NULL,
    `hashtags` TEXT DEFAULT NULL,
    `user_mentions` TEXT DEFAULT NULL,
    `place` TEXT DEFAULT NULL,
    `place_coordinate` VARCHAR(100) DEFAULT NULL,
    `score` TEXT NOT NULL,
    PRIMARY KEY (`id`)
);
