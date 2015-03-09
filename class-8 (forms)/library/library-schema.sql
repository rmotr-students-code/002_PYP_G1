drop table if exists country;
create table country (
  id integer primary key autoincrement,
  name text not null default "UNKNOWN"
);

drop table if exists author;
create table author(
  id integer primary key autoincrement,
  country_id integer,
  name text not null default "UNKNOWN"
);

drop table if exists book;
create table book(
  id integer primary key autoincrement,
  author_id integer,
  title text not null,
  isbn text not null unique
);