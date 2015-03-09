drop table if exists country;
create table country(
  id integer autoincrement
  name text not null default "UNKNOWN"
  primary key(id)
);

drop table if exists author;
create table author(
  id integer autoincrement,
  country_id integer,
  name text not null default "UNKNOWN"
  foreign key(country_id) references country(id)
  primary key(id)
);

drop table if exists book;
create table book (
  id integer autoincrement,
  author_id integer,
  title text not null,
  isbn text not null unique
  foreign key(author_id) references author(id)
  primary key(id)
);