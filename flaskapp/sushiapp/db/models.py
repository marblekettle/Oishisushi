from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
	pass

class MenuItem(Base):
	__tablename__ = 'menu_item'
	item_id = Column(Integer, primary_key=True)
	name = Column(String(100))
	price = Column(Integer)
