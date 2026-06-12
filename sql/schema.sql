create database smart_spend;
go

use smart_spend;
go

create table users(
    user_id int primary key identity(1,1),
    name varchar(100),
    email varchar(100),
    password varchar(100)
);

create table income(
    income_id int primary key identity(1,1),
    user_id int,
    amount decimal(10,2),
    source varchar(200),
    income_date date,
    foreign key(user_id) references users(user_id)
);

create table expense(
    expense_id int primary key identity(1,1),
    user_id int,
    amount decimal(10,2),
    category varchar(100),
    description varchar(200),
    expense_date date,
    foreign key(user_id) references users(user_id)
);