# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, LargeBinary, SmallInteger, String, Text, Uuid, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  March 14, 2025 00:22:13
# Database: postgresql://postgres:p@10.0.0.249/postgres
# Dialect:  postgresql
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.postgresql import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Category(Base):  # type: ignore
    __tablename__ = 'categories'
    _s_collection_name = 'Category'  # type: ignore

    category_id = Column('category_id', SmallInteger, server_default=text("0"), primary_key=True, quote = True)
    category_name = Column('category_name', String(15), nullable=False, quote = True)
    description = Column('description', Text, quote = True)
    picture = Column('picture', LargeBinary, quote = True)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="category")



class CustomerDemographic(Base):  # type: ignore
    __tablename__ = 'customer_demographics'
    _s_collection_name = 'CustomerDemographic'  # type: ignore

    customer_type_id = Column('customer_type_id', String(5), primary_key=True, quote = True)
    customer_desc = Column('customer_desc', Text, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerCustomerDemoList : Mapped[List["CustomerCustomerDemo"]] = relationship(back_populates="customer_type")



class Customer(Base):  # type: ignore
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore

    customer_id = Column('customer_id', String(5), primary_key=True, quote = True)
    company_name = Column('company_name', String(40), nullable=False, quote = True)
    contact_name = Column('contact_name', String(30), quote = True)
    contact_title = Column('contact_title', String(30), quote = True)
    address = Column('address', String(60), quote = True)
    city = Column('city', String(15), quote = True)
    region = Column('region', String(15), quote = True)
    postal_code = Column('postal_code', String(10), quote = True)
    country = Column('country', String(15), quote = True)
    phone = Column('phone', String(24), quote = True)
    fax = Column('fax', String(24), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerCustomerDemoList : Mapped[List["CustomerCustomerDemo"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class DeviceType(Base):  # type: ignore
    __tablename__ = 'device_types'
    _s_collection_name = 'DeviceType'  # type: ignore

    unique_id = Column('unique_id', Integer, server_default=text("nextval('device_types_unique_id_seq'::regclass)"), primary_key=True, quote = True)
    device_type = Column('device_type', Text, nullable=False, unique=True, quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)
    DeviceList : Mapped[List["Device"]] = relationship(back_populates="device_type")



class Employee(Base):  # type: ignore
    __tablename__ = 'employees'
    _s_collection_name = 'Employee'  # type: ignore

    employee_id = Column('employee_id', SmallInteger, primary_key=True, quote = True)
    last_name = Column('last_name', String(20), nullable=False, quote = True)
    first_name = Column('first_name', String(10), nullable=False, quote = True)
    title = Column('title', String(30), quote = True)
    title_of_courtesy = Column('title_of_courtesy', String(25), quote = True)
    birth_date = Column('birth_date', Date, quote = True)
    hire_date = Column('hire_date', Date, quote = True)
    address = Column('address', String(60), quote = True)
    city = Column('city', String(15), quote = True)
    region = Column('region', String(15), quote = True)
    postal_code = Column('postal_code', String(10), quote = True)
    country = Column('country', String(15), quote = True)
    home_phone = Column('home_phone', String(24), quote = True)
    extension = Column('extension', String(4), quote = True)
    photo = Column('photo', LargeBinary, quote = True)
    notes = Column('notes', Text, quote = True)
    reports_to = Column('reports_to', ForeignKey('employees.employee_id'), quote = True)
    photo_path = Column('photo_path', String(255), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Employee : Mapped["Employee"] = relationship(remote_side=[employee_id], back_populates=("EmployeeList"))

    # child relationships (access children)
    EmployeeList : Mapped[List["Employee"]] = relationship(back_populates="Employee")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="employee")
    EmployeeTerritoryList : Mapped[List["EmployeeTerritory"]] = relationship(back_populates="employee")



class EquipmentType(Base):  # type: ignore
    __tablename__ = 'equipment_types'
    _s_collection_name = 'EquipmentType'  # type: ignore

    unique_id = Column('unique_id', Integer, server_default=text("nextval('equipment_types_unique_id_seq'::regclass)"), primary_key=True, quote = True)
    equipment_type = Column('equipment_type', Text, nullable=False, unique=True, quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)
    EquipmentList : Mapped[List["Equipment"]] = relationship(back_populates="equipment_type")



class EventSubjectsType(Base):  # type: ignore
    __tablename__ = 'event_subjects_types'
    _s_collection_name = 'EventSubjectsType'  # type: ignore

    unique_id = Column('unique_id', Integer, server_default=text("nextval('event_subjects_types_unique_id_seq'::regclass)"), primary_key=True, quote = True)
    event_subject_type = Column('event_subject_type', Text, nullable=False, unique=True, quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)



class EventType(Base):  # type: ignore
    __tablename__ = 'event_types'
    _s_collection_name = 'EventType'  # type: ignore

    unique_id = Column('unique_id', Integer, server_default=text("nextval('event_types_unique_id_seq'::regclass)"), primary_key=True, quote = True)
    event_type = Column('event_type', Text, nullable=False, unique=True, quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)
    EventsLogList : Mapped[List["EventsLog"]] = relationship(back_populates="event_type")



class LogLevel(Base):  # type: ignore
    __tablename__ = 'log_levels'
    _s_collection_name = 'LogLevel'  # type: ignore

    unique_id = Column('unique_id', Integer, server_default=text("nextval('log_levels_unique_id_seq'::regclass)"), primary_key=True, quote = True)
    log_level = Column('log_level', Text, nullable=False, unique=True, quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)
    EventsLogList : Mapped[List["EventsLog"]] = relationship(back_populates="log_level")



class Region(Base):  # type: ignore
    __tablename__ = 'region'
    _s_collection_name = 'Region'  # type: ignore

    region_id = Column('region_id', SmallInteger, primary_key=True, quote = True)
    region_description = Column('region_description', String(60), nullable=False, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    TerritoryList : Mapped[List["Territory"]] = relationship(back_populates="region")



class SensorsLine(Base):  # type: ignore
    __tablename__ = 'sensors_lines'
    _s_collection_name = 'SensorsLine'  # type: ignore

    unique_id = Column('unique_id', Integer, server_default=text("nextval('sensors_lines_unique_id_seq'::regclass)"), primary_key=True, quote = True)
    uuid_id = Column('uuid_id', Uuid, server_default=text("gen_random_uuid()"), quote = True)
    is_digital = Column('is_digital', Boolean, server_default=text("true"), quote = True)
    sensor_line_label = Column('sensor_line_label', Text, nullable=False, unique=True, quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)
    DeviceSensorsLineList : Mapped[List["DeviceSensorsLine"]] = relationship(back_populates="sensor_line")



class Shipper(Base):  # type: ignore
    __tablename__ = 'shippers'
    _s_collection_name = 'Shipper'  # type: ignore

    shipper_id = Column('shipper_id', SmallInteger, primary_key=True, quote = True)
    company_name = Column('company_name', String(40), nullable=False, quote = True)
    phone = Column('phone', String(24), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="shipper")



class Supplier(Base):  # type: ignore
    __tablename__ = 'suppliers'
    _s_collection_name = 'Supplier'  # type: ignore

    supplier_id = Column('supplier_id', SmallInteger, primary_key=True, quote = True)
    company_name = Column('company_name', String(40), nullable=False, quote = True)
    contact_name = Column('contact_name', String(30), quote = True)
    contact_title = Column('contact_title', String(30), quote = True)
    address = Column('address', String(60), quote = True)
    city = Column('city', String(15), quote = True)
    region = Column('region', String(15), quote = True)
    postal_code = Column('postal_code', String(10), quote = True)
    country = Column('country', String(15), quote = True)
    phone = Column('phone', String(24), quote = True)
    fax = Column('fax', String(24), quote = True)
    homepage = Column('homepage', Text, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="supplier")



class UsState(Base):  # type: ignore
    __tablename__ = 'us_states'
    _s_collection_name = 'UsState'  # type: ignore

    state_id = Column('state_id', SmallInteger, primary_key=True, quote = True)
    state_name = Column('state_name', String(100), quote = True)
    state_abbr = Column('state_abbr', String(2), quote = True)
    state_region = Column('state_region', String(50), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)



class Vessel(Base):  # type: ignore
    __tablename__ = 'vessels'
    _s_collection_name = 'Vessel'  # type: ignore

    unique_id = Column('unique_id', Integer, server_default=text("nextval('vessels_unique_id_seq'::regclass)"), primary_key=True, quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    vessel_name = Column('vessel_name', Text, nullable=False, quote = True)
    imo_number = Column('imo_number', Text, nullable=False, quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)
    VesselEquipmentList : Mapped[List["VesselEquipment"]] = relationship(back_populates="vessel")



class CustomerCustomerDemo(Base):  # type: ignore
    __tablename__ = 'customer_customer_demo'
    _s_collection_name = 'CustomerCustomerDemo'  # type: ignore

    customer_id = Column('customer_id', ForeignKey('customers.customer_id'), primary_key=True, nullable=False, quote = True)
    customer_type_id = Column('customer_type_id', ForeignKey('customer_demographics.customer_type_id'), primary_key=True, nullable=False, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("CustomerCustomerDemoList"))
    customer_type : Mapped["CustomerDemographic"] = relationship(back_populates=("CustomerCustomerDemoList"))

    # child relationships (access children)



class Device(Base):  # type: ignore
    __tablename__ = 'devices'
    _s_collection_name = 'Device'  # type: ignore

    unique_id = Column('unique_id', Integer, server_default=text("nextval('devices_unique_id_seq'::regclass)"), primary_key=True, quote = True)
    ip_address = Column('ip_address', Text, nullable=False, unique=True, quote = True)
    device_type_id = Column('device_type_id', ForeignKey('device_types.unique_id'), quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)

    # parent relationships (access parent)
    device_type : Mapped["DeviceType"] = relationship(back_populates=("DeviceList"))

    # child relationships (access children)
    DeviceSensorsLineList : Mapped[List["DeviceSensorsLine"]] = relationship(back_populates="device")



class Equipment(Base):  # type: ignore
    __tablename__ = 'equipment'
    _s_collection_name = 'Equipment'  # type: ignore

    unique_id = Column('unique_id', Integer, server_default=text("nextval('equipment_unique_id_seq'::regclass)"), primary_key=True, quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    equipment_type_id = Column('equipment_type_id', ForeignKey('equipment_types.unique_id'), quote = True)
    equipment_name = Column('equipment_name', Text, nullable=False, quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)

    # parent relationships (access parent)
    equipment_type : Mapped["EquipmentType"] = relationship(back_populates=("EquipmentList"))

    # child relationships (access children)
    VesselEquipmentList : Mapped[List["VesselEquipment"]] = relationship(back_populates="equipment")



class EventsLog(Base):  # type: ignore
    __tablename__ = 'events_log'
    _s_collection_name = 'EventsLog'  # type: ignore

    subject_of_change_id = Column('subject_of_change_id', Integer, primary_key=True, nullable=False, quote = True)
    subject_of_change_type_id = Column('subject_of_change_type_id', Integer, primary_key=True, nullable=False, quote = True)
    event_type_id = Column('event_type_id', ForeignKey('event_types.unique_id'), quote = True)
    previous_state_value = Column('previous_state_value', Text, quote = True)
    new_state_value = Column('new_state_value', Text, quote = True)
    log_level_id = Column('log_level_id', ForeignKey('log_levels.unique_id'), quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    event_type : Mapped["EventType"] = relationship(back_populates=("EventsLogList"))
    log_level : Mapped["LogLevel"] = relationship(back_populates=("EventsLogList"))

    # child relationships (access children)



class Order(Base):  # type: ignore
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore

    order_id = Column('order_id', SmallInteger, primary_key=True, quote = True)
    customer_id = Column('customer_id', ForeignKey('customers.customer_id'), quote = True)
    employee_id = Column('employee_id', ForeignKey('employees.employee_id'), quote = True)
    order_date = Column('order_date', Date, quote = True)
    required_date = Column('required_date', Date, quote = True)
    shipped_date = Column('shipped_date', Date, quote = True)
    ship_via = Column('ship_via', ForeignKey('shippers.shipper_id'), quote = True)
    freight = Column('freight', Float, quote = True)
    ship_name = Column('ship_name', String(40), quote = True)
    ship_address = Column('ship_address', String(60), quote = True)
    ship_city = Column('ship_city', String(15), quote = True)
    ship_region = Column('ship_region', String(15), quote = True)
    ship_postal_code = Column('ship_postal_code', String(10), quote = True)
    ship_country = Column('ship_country', String(15), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))
    employee : Mapped["Employee"] = relationship(back_populates=("OrderList"))
    shipper : Mapped["Shipper"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="order")



class Product(Base):  # type: ignore
    __tablename__ = 'products'
    _s_collection_name = 'Product'  # type: ignore

    product_id = Column('product_id', SmallInteger, primary_key=True, quote = True)
    product_name = Column('product_name', String(40), nullable=False, quote = True)
    supplier_id = Column('supplier_id', ForeignKey('suppliers.supplier_id'), quote = True)
    category_id = Column('category_id', ForeignKey('categories.category_id'), quote = True)
    quantity_per_unit = Column('quantity_per_unit', String(20), quote = True)
    unit_price = Column('unit_price', Float, quote = True)
    units_in_stock = Column('units_in_stock', SmallInteger, quote = True)
    units_on_order = Column('units_on_order', SmallInteger, quote = True)
    reorder_level = Column('reorder_level', SmallInteger, quote = True)
    discontinued = Column('discontinued', Integer, nullable=False, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    category : Mapped["Category"] = relationship(back_populates=("ProductList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("ProductList"))

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="product")



class Territory(Base):  # type: ignore
    __tablename__ = 'territories'
    _s_collection_name = 'Territory'  # type: ignore

    territory_id = Column('territory_id', String(20), primary_key=True, quote = True)
    territory_description = Column('territory_description', String(60), nullable=False, quote = True)
    region_id = Column('region_id', ForeignKey('region.region_id'), nullable=False, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    region : Mapped["Region"] = relationship(back_populates=("TerritoryList"))

    # child relationships (access children)
    EmployeeTerritoryList : Mapped[List["EmployeeTerritory"]] = relationship(back_populates="territory")



class DeviceSensorsLine(Base):  # type: ignore
    __tablename__ = 'device_sensors_lines'
    _s_collection_name = 'DeviceSensorsLine'  # type: ignore

    device_id = Column('device_id', ForeignKey('devices.unique_id'), primary_key=True, nullable=False, quote = True)
    sensor_line_id = Column('sensor_line_id', ForeignKey('sensors_lines.unique_id'), primary_key=True, nullable=False, quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    device : Mapped["Device"] = relationship(back_populates=("DeviceSensorsLineList"))
    sensor_line : Mapped["SensorsLine"] = relationship(back_populates=("DeviceSensorsLineList"))

    # child relationships (access children)



class EmployeeTerritory(Base):  # type: ignore
    __tablename__ = 'employee_territories'
    _s_collection_name = 'EmployeeTerritory'  # type: ignore

    employee_id = Column('employee_id', ForeignKey('employees.employee_id'), primary_key=True, nullable=False, quote = True)
    territory_id = Column('territory_id', ForeignKey('territories.territory_id'), primary_key=True, nullable=False, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    employee : Mapped["Employee"] = relationship(back_populates=("EmployeeTerritoryList"))
    territory : Mapped["Territory"] = relationship(back_populates=("EmployeeTerritoryList"))

    # child relationships (access children)



class OrderDetail(Base):  # type: ignore
    __tablename__ = 'order_details'
    _s_collection_name = 'OrderDetail'  # type: ignore

    order_id = Column('order_id', ForeignKey('orders.order_id'), primary_key=True, nullable=False, quote = True)
    product_id = Column('product_id', ForeignKey('products.product_id'), primary_key=True, nullable=False, quote = True)
    unit_price = Column('unit_price', Float, nullable=False, quote = True)
    quantity = Column('quantity', SmallInteger, nullable=False, quote = True)
    discount = Column('discount', Float, nullable=False, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderDetailList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderDetailList"))

    # child relationships (access children)



class VesselEquipment(Base):  # type: ignore
    __tablename__ = 'vessel_equipment'
    _s_collection_name = 'VesselEquipment'  # type: ignore

    vessel_id = Column('vessel_id', ForeignKey('vessels.unique_id'), primary_key=True, nullable=False, quote = True)
    equipment_id = Column('equipment_id', ForeignKey('equipment.unique_id'), primary_key=True, nullable=False, quote = True)
    create_date = Column('create_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    update_date = Column('update_date', DateTime, server_default=text("CURRENT_TIMESTAMP"), quote = True)
    is_inactive = Column('is_inactive', Boolean, server_default=text("false"), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    equipment : Mapped["Equipment"] = relationship(back_populates=("VesselEquipmentList"))
    vessel : Mapped["Vessel"] = relationship(back_populates=("VesselEquipmentList"))

    # child relationships (access children)
