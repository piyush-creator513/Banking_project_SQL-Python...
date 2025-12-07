create database bank530
create table superadmin(sid varchar(10) primary key,
spwd varchar(20))

insert into superadmin values ('super1','12345')
insert into superadmin values ('super2','45678')

select*from superadmin

---admin

create table admin (aid varchar(10) primary key,
apwd varchar(20),
sid varchar(10)foreign key references superadmin(sid))

select * from admin

-- branches(bid primary key, bname, city, aid foreign key,
--contact, mail)
create table branches(bid varchar(10) primary key,
bname varchar(20) unique not null,
city varchar(20) not null,
bcontact varchar(10) unique not null
check(len(bcontact)=10 and bcontact not Like('%[^0-9]%')
and LEFT(bcontact,1) in ('9','8','7','6')),

bemail varchar(30) unique not null
check (bemail like '_%@%.%' and bemail not like '% %'))


-------employee

create table Employee (eid varchar(10) primary key,
ename varchar(20),
emob varchar(10) unique not null
check(len(emob)=10 and emob not Like('%[^0-9]%')
and LEFT(emob,1) in ('9','8','7','6')),

email varchar(30) unique not null
check (email like '_%@%.%' and email not like '% %'),
address varchar(20) not null,
esal int not null
check (esal >= 15000),
post varchar(10) not null
check(post in('manager','po','clerk','cashier')),
bid varchar (10) foreign key references branches (bid))


---customer

create table customer (cid int primary key identity(1,1),
cname varchar(20),
cmob varchar(10) unique not null
check (len(cmob)=10 and cmob not Like('%[^0-9]%')
and LEFT(cmob,1) in ('9','8','7','6')),

cmail varchar(30) unique not null
check (cmail like '_%@%.%' and cmail not like '% %'),
address varchar(20) not null,
aadhar varchar(12) unique not null
check(len(aadhar)=12 and aadhar not like ('%[^0-9]%')),
bid varchar (10) foreign key references branches (bid))

--primary key,foreign key, bid foreign key, balance)

---account 

create table account (acc_no int primary key,
acc_type varchar(15) not null
check(acc_type in('Savings','current')),
cid int  foreign key references customer(cid),
bid varchar(10) foreign key references branches(bid),
balance int not null)


----transaction

create table acc_transaction (tid int primary key identity(1,1),
amount int not null,
amount_type varchar (10) check(amount_type in ('credit','debit')),
acc_no int foreign key references account(acc_no))



ALTER TABLE transactions
DROP CONSTRAINT FK__transacti__acc_n__5BE2A6F2;


drop table transactions

select * from acc_transaction

select * from branches

select * from Employee

select * from customer

select * from account