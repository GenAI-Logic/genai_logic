# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class Customer(Base):
    """description: Model for storing customer information including balance and credit limit."""
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    balance = Column(DECIMAL)
    credit_limit = Column(DECIMAL)

class Order(Base):
    """description: Model for storing order information including link to customer and notes."""
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    amount_total = Column(DECIMAL)
    date_shipped = Column(Date)
    notes = Column(String(200))

class Item(Base):
    """description: Model for storing item details including quantity and calculated amount."""
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
    unit_price = Column(DECIMAL)
    amount = Column(DECIMAL)

class Product(Base):
    """description: Model for storing product information including name and unit price."""
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    unit_price = Column(DECIMAL)

class OrderDetail(Base):
    """description: Model for storing order detail linking orders and items."""
    __tablename__ = 'order_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    item_id = Column(Integer, ForeignKey('item.id'))


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    customer_1 = Customer(name="Alice", balance=Decimal('500.00'), credit_limit=Decimal('1000.00'))
    customer_2 = Customer(name="Bob", balance=Decimal('1200.00'), credit_limit=Decimal('1500.00'))
    customer_3 = Customer(name="Charlie", balance=Decimal('950.00'), credit_limit=Decimal('950.00'))
    customer_4 = Customer(name="Dana", balance=Decimal('300.00'), credit_limit=Decimal('800.00'))
    order_1 = Order(customer_id=1, amount_total=Decimal('200'), date_shipped=None, notes="Urgent")
    order_2 = Order(customer_id=2, amount_total=Decimal('300'), date_shipped=date(2023, 7, 15), notes="Express")
    order_3 = Order(customer_id=3, amount_total=Decimal('150'), date_shipped=None, notes="Regular")
    order_4 = Order(customer_id=4, amount_total=Decimal('250'), date_shipped=date(2023, 7, 10), notes="Overnight")
    item_1 = Item(order_id=1, product_id=1, quantity=10, unit_price=Decimal('10'), amount=Decimal('100'))
    item_2 = Item(order_id=1, product_id=2, quantity=5, unit_price=Decimal('20'), amount=Decimal('100'))
    item_3 = Item(order_id=2, product_id=3, quantity=2, unit_price=Decimal('150'), amount=Decimal('300'))
    item_4 = Item(order_id=3, product_id=4, quantity=3, unit_price=Decimal('50'), amount=Decimal('150'))
    
    
    
    session.add_all([customer_1, customer_2, customer_3, customer_4, order_1, order_2, order_3, order_4, item_1, item_2, item_3, item_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
