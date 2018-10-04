-- Create a Database
create database BobcatBazaar;

use BobcatBazaar;

-- create the Users table and the necessary columns
create table Users (
        Username		varchar(32) not null primary key,
        Email				varchar(32) not null,
        Password		varchar(32) not null
);

create table Postings (
		Title					varchar(65) not null,
        Price				DECIMAL(13,2) NOT NULL,
        Location			varchar(55) not null,
        Description		TEXT not null
);

