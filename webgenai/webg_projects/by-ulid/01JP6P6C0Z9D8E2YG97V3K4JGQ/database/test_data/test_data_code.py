import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not 986618080692904089 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_customer_1 = Customer(name='Customer 1', balance=150, credit_limit=1000)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(986618080692904089)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -9150195543761546614 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_customer_2 = Customer(name='Customer 2', balance=275, credit_limit=750)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-9150195543761546614)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6497188083510282323 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_customer_3 = Customer(name='Customer 3', balance=150, credit_limit=1500)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6497188083510282323)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4712769071676319027 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_customer_4 = Customer(name='Customer 4', balance=0, credit_limit=1200)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4712769071676319027)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2956547458942946431 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_order_1 = Order(customer_id=1, notes='Order 1 notes', amount_total=150)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2956547458942946431)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 9025600277600652913 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_order_2 = Order(customer_id=2, notes='Order 2 notes', amount_total=225)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(9025600277600652913)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7680182611158851186 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_order_3 = Order(customer_id=2, notes='Order 3 notes', amount_total=50)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7680182611158851186)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4487594248046502025 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_order_4 = Order(customer_id=3, notes='Order 4 notes', amount_total=150)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4487594248046502025)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1710820151041777738 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_item_1 = Item(order_id=1, product_id=1, quantity=3, unit_price=50, amount=150)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1710820151041777738)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1268110969106386283 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_item_2 = Item(order_id=2, product_id=2, quantity=2, unit_price=25, amount=50)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1268110969106386283)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4331592040373619905 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_item_3 = Item(order_id=3, product_id=3, quantity=3, unit_price=75, amount=225)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4331592040373619905)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4406069320905132547 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_item_4 = Item(order_id=4, product_id=1, quantity=3, unit_price=50, amount=150)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4406069320905132547)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8663365809587626994 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_product_1 = Product(name='Product 1', unit_price=50)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8663365809587626994)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7637221754838568506 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_product_2 = Product(name='Product 2', unit_price=25)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7637221754838568506)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6132301331198913248 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_product_3 = Product(name='Product 3', unit_price=75)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6132301331198913248)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5688189104170135738 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_product_4 = Product(name='Product 4', unit_price=100)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5688189104170135738)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
