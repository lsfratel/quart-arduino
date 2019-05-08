from sqlite3 import dbapi2 as sqlite3
from datetime import datetime

def connect_db(p):
    engine = sqlite3.connect(p)
    engine.row_factory = sqlite3.Row
    return engine

def format_date(s):
    return datetime.strptime(s, '%d/%m/%Y %H:%M:%S')