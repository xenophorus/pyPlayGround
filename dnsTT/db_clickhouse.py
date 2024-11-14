from sqlalchemy import create_engine, Column, MetaData
from


class Base(DeclarativeBase):
    ...


class Cities(Base):
    __tablename__ = "cities"

    city_uuid = Column(UUID, primary_key=True)
    city_name = Column(String)




class Products(Base):
    __tablename__ = "products"

    product_uuid = Column(UUID, primary_key=True)
    product_name = Column(String)


class Branches(Base):
    __tablename__ = "branches"

    branch_uuid = Column(UUID, primary_key=True)
    branch_name = Column(String)
    city_uuid = Column(UUID, ForeignKey("cities.city_uuid"))
    branch_short_name = Column(String)
    region = Column(String)


class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    sale_datetime = Column(DateTime)
    branch_uuid = Column(UUID, ForeignKey("branches.branch_uuid"))
    product_uuid = Column(UUID, ForeignKey("products.product_uuid"))
    quantity = Column(Float)
    revenue = Column(Float)


class PostgresDB:
    def __init__(self):
        db_uri = "postgresql+psycopg2://alex:21779835@127.0.0.1:5432/dns_tt"
        engine = create_engine(db_uri)
        metadata = Base.metadata

