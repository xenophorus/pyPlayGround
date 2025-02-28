create database st_course1;

create table st_course1.district (
    OrderID String,
    DeliveryDistrictName String
) ENGINE=Log;

SET format_csv_delimiter = ';';

create table st_course1.orders (
    OrderID String,
    OrderDate String,
    ProductName String,
    ProductBrand String,
    ProductSubcategory String,
    ProductCategory String,
    DeliveryType String,
    PaymentType String,
    ClientGender String,
    Sales Int32,
    ClientStatus String,
    ShopName String,
    ShopAddress String,
    ShopAddressCoord String
) ENGINE=Log;

SET format_csv_delimiter = ';';

select * from st_course1.district;
select * from st_course1.orders;

-- clickhouse-client --format_csv_delimiter ";" -q "INSERT INTO st_course1.district FORMAT CSVWithNames" < district_conv.csv
-- clickhouse-client --format_csv_delimiter ";" -q "INSERT INTO st_course1.orders FORMAT CSVWithNames" < orders_conv.csv

create database dns_data;

create database st_course;

use st_course;

CREATE TABLE titanic (
    PassengerId Int64,
    Survived Int8,
    Pclass Int16,
    Name String,
    Sex String,
    Age String,
    SibSp  Int8,
    Parch Int32,
    Ticket String,
    Fare String,
    Cabin  String,
    Embarked  String)
ENGINE=TinyLog;

INSERT INTO titanic
SELECT * FROM url('https://raw.githubusercontent.com/dmitrii12334/clickhouse/main/titanic', CSVWithNames, 'PassengerId Int64, Survived Int8, Pclass Int16, Name String, Sex String, Age String, SibSp Int8, Parch Int32, Ticket String, Fare String, Cabin  String, Embarked  String');

select * from titanic;

CREATE TABLE video_game_sales (
    Rank UInt32,
    Name String,
    Platform String,
    Year String,
    Genre String,
    Publisher String,
    NA_Sales Float32,
    EU_Sales Float32,
    JP_Sales Float32,
    Other_Sales Float32,
    Global_Sales Float32
) ENGINE = Log;

INSERT INTO video_game_sales SELECT * FROM url('https://raw.githubusercontent.com/dmitrii12334/clickhouse/main/vgsale', CSVWithNames, 'Rank UInt32,
    Name String,
    Platform String,
    Year String,
    Genre String,
    Publisher String,
    NA_Sales Float32,
    EU_Sales Float32,
    JP_Sales Float32,
    Other_Sales Float32,
    Global_Sales Float32');

SELECT * from video_game_sales;

use dns_data;

create table branches (
    num Int32,
    uuid String,
    name String,
    city String,
    short_name String,
    region String
) ENGINE = Log
;

create table cities (
    num Int32,
    uuid String,
    name String
)ENGINE = Log
;

create table products (
    num Int32,
    uuid String,
    name String
)ENGINE = Log
;

create table sales (
    num Int32,
    date_time String,
    branch_uuid String,
    product_uuid String,
    quantity Float32,
    sale Float64
) ENGINE = Log
;

select * from branches;

-- clickhouse-client -h localhost --port 19000 -u alex --password 21779835 -q "INSERT INTO dns_data.branches FORMAT CSVWithNames" < t_branches.csv
-- clickhouse-client -h localhost --port 19000 -u alex --password 21779835 -q "INSERT INTO dns_data.cities FORMAT CSVWithNames" < t_cities.csv
-- clickhouse-client -h localhost --port 19000 -u alex --password 21779835 -q "INSERT INTO dns_data.products FORMAT CSVWithNames" < t_products.csv
-- clickhouse-client -h localhost --port 19000 -u alex --password 21779835 -q "INSERT INTO dns_data.sales FORMAT CSVWithNames" < t_sales.csv


