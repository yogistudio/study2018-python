"""
邮校学习
0425
sqllite
"""

from sqlalchemy import Column, String, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'  # 表的名字
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


engine = create_engine(r'sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.id == '5').one()
print('type:', type(user))
print('name:', user.name)
session.close()
