/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : lmdb

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-05-03 12:43:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', 'admin', 'admin', '2020-05-02 14:57:36');
INSERT INTO `admin` VALUES ('2', 'root', 'root', '2020-05-02 16:18:23');
INSERT INTO `admin` VALUES ('3', 'test', 'test', '2020-05-02 20:06:51');
INSERT INTO `admin` VALUES ('4', 'test1', 'test1', '2020-05-03 10:39:19');

-- ----------------------------
-- Table structure for `alembic_version`
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('3d7aac9ff6de');

-- ----------------------------
-- Table structure for `message`
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `create_time` datetime NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of message
-- ----------------------------
INSERT INTO `message` VALUES ('10', 'python 好难啊', '2020-05-03 00:34:19', '2');
INSERT INTO `message` VALUES ('11', '我饭卡丢了，怎么办！', '2020-05-03 12:17:26', '1');
INSERT INTO `message` VALUES ('12', '想吃螺蛳粉！', '2020-05-03 12:18:46', '1');
INSERT INTO `message` VALUES ('13', '想吃螺蛳粉！', '2020-05-03 12:19:13', '1');
INSERT INTO `message` VALUES ('14', '想吃海底捞！', '2020-05-03 12:24:09', '1');

-- ----------------------------
-- Table structure for `message_to_tag`
-- ----------------------------
DROP TABLE IF EXISTS `message_to_tag`;
CREATE TABLE `message_to_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message_id` int(11) DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `message_id` (`message_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `message_to_tag_ibfk_1` FOREIGN KEY (`message_id`) REFERENCES `message` (`id`),
  CONSTRAINT `message_to_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of message_to_tag
-- ----------------------------
INSERT INTO `message_to_tag` VALUES ('4', '10', '3');
INSERT INTO `message_to_tag` VALUES ('7', '11', '3');
INSERT INTO `message_to_tag` VALUES ('8', '11', '8');
INSERT INTO `message_to_tag` VALUES ('9', '12', '3');
INSERT INTO `message_to_tag` VALUES ('10', '12', '4');
INSERT INTO `message_to_tag` VALUES ('11', '12', '5');
INSERT INTO `message_to_tag` VALUES ('12', '13', '3');
INSERT INTO `message_to_tag` VALUES ('13', '13', '5');
INSERT INTO `message_to_tag` VALUES ('14', '14', '9');

-- ----------------------------
-- Table structure for `tag`
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `create_time` datetime NOT NULL,
  `admin_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `admin_id` (`admin_id`),
  CONSTRAINT `tag_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES ('3', 'tag3', '2020-05-02 17:12:44', '1');
INSERT INTO `tag` VALUES ('4', '数学', '2020-05-02 20:26:13', '1');
INSERT INTO `tag` VALUES ('5', '英语', '2020-05-02 20:26:26', '1');
INSERT INTO `tag` VALUES ('6', 'python', '2020-05-02 20:26:55', '1');
INSERT INTO `tag` VALUES ('8', '寻物启事', '2020-05-03 10:52:47', '1');
INSERT INTO `tag` VALUES ('9', '吃货', '2020-05-03 12:23:59', '1');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'user1', 'user1', '2020-05-02 15:36:34');
INSERT INTO `user` VALUES ('2', 'test', 'test', '2020-05-02 23:08:04');
