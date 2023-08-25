CREATE TABLE `comic_page` (
    `page_id` int NOT NULL AUTO_INCREMENT,
    `chapter_id` int NOT NULL,
    `page_number` int DEFAULT NULL,
    `release_date` date NOT NULL,
    `description` text,
    `page_position` varchar(1) DEFAULT NULL,
    `image_name` varchar(30) DEFAULT NULL COMMENT 'name of the image in the pages folder',
    `status` varchar(1) DEFAULT NULL,
    `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`page_id`),
    UNIQUE KEY `uq_chapter_page_number` (`chapter_id`,`page_number`),
    CONSTRAINT `comic_page_ibfk_1` FOREIGN KEY (`chapter_id`) REFERENCES `comic_chapter` (`chapter_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

