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
        if not 1698014273160378176 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer_1 = Customer(name="Alice", balance=Decimal('500.00'), credit_limit=Decimal('1000.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1698014273160378176)
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
        if not -7442373639803259716 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer_2 = Customer(name="Bob", balance=Decimal('1200.00'), credit_limit=Decimal('1500.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7442373639803259716)
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
        if not 5831404575893430764 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer_3 = Customer(name="Charlie", balance=Decimal('950.00'), credit_limit=Decimal('950.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5831404575893430764)
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
        if not -3232052542524640673 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer_4 = Customer(name="Dana", balance=Decimal('300.00'), credit_limit=Decimal('800.00'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3232052542524640673)
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
        if not 2137750339211209300 in succeeded_hashes:  # avoid duplicate inserts
            instance = order_1 = Order(customer_id=1, amount_total=Decimal('200'), date_shipped=None, notes="Urgent")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2137750339211209300)
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
        if not 114123910236501277 in succeeded_hashes:  # avoid duplicate inserts
            instance = order_2 = Order(customer_id=2, amount_total=Decimal('300'), date_shipped=date(2023, 7, 15), notes="Express")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(114123910236501277)
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
        if not -6307408125493599067 in succeeded_hashes:  # avoid duplicate inserts
            instance = order_3 = Order(customer_id=3, amount_total=Decimal('150'), date_shipped=None, notes="Regular")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6307408125493599067)
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
        if not -5624793076223501278 in succeeded_hashes:  # avoid duplicate inserts
            instance = order_4 = Order(customer_id=4, amount_total=Decimal('250'), date_shipped=date(2023, 7, 10), notes="Overnight")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5624793076223501278)
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
        if not -4298037571176785573 in succeeded_hashes:  # avoid duplicate inserts
            instance = item_1 = Item(order_id=1, product_id=1, quantity=10, unit_price=Decimal('10'), amount=Decimal('100'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4298037571176785573)
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
        if not -471437123290716916 in succeeded_hashes:  # avoid duplicate inserts
            instance = item_2 = Item(order_id=1, product_id=2, quantity=5, unit_price=Decimal('20'), amount=Decimal('100'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-471437123290716916)
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
        if not -3218049060194483288 in succeeded_hashes:  # avoid duplicate inserts
            instance = item_3 = Item(order_id=2, product_id=3, quantity=2, unit_price=Decimal('150'), amount=Decimal('300'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3218049060194483288)
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
        if not 3823588729517148177 in succeeded_hashes:  # avoid duplicate inserts
            instance = item_4 = Item(order_id=3, product_id=4, quantity=3, unit_price=Decimal('50'), amount=Decimal('150'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3823588729517148177)
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
