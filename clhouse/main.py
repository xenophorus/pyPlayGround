from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import ForeignKey, String, Integer, UUID, Double, Column, select

class Base(DeclarativeBase):
    pass

class Cities(Base):
    __tablename__ = 'cities'
    num: Mapped[Integer] = Column(Integer)
    uuid: Mapped[UUID] = Column(UUID, primary_key=True)
    name: Mapped[String] = Column(String)

class Branches(Base):
    __tablename__ = 'branches'
    num: Mapped[Integer] = Column(Integer)
    uuid: Mapped[UUID] = Column(UUID, primary_key=True)
    name: Mapped[String] = Column(String)
    city: Mapped[UUID] = Column(UUID, ForeignKey('cities.uuid'))
    short_name: Mapped[String] = Column(String)
    region: Mapped[String] = Column(String)


uri = "clickhouse+http://alex:21779835@localhost:18123/dns_data"
engine = create_engine(uri)

# Base.metadata.create_all(engine)

with Session(engine) as session:
    # result = session.query(Cities).join(Branches).join(Branches.city)
    query = select(Cities.name, Branches.short_name)\
        .join(Branches)\
        .order_by(Cities.name, Branches.short_name)
    result = session.execute(query).all()

for row in result:
    print(row)


#
# import clickhouse_connect
#
# client = clickhouse_connect.get_client(
#     host="localhost",
#     port=18123,
#     username="alex",
#     password="21779835",
#     database="dns_data"
#
# )
#
# res = client.query('select uuid, name from cities')
#
# print(res.row_count)
# print(res.first_row)
# print(res.result_rows)