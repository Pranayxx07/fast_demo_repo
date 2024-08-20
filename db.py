from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine




db_str = "postgresql://doadmin:AVNS_EGsxiixbLnXyUP42wkt@localhost:25060/defaultdb"

engine = create_engine(db_str)

BASE = declarative_base()


SESSION_LOCAL = sessionmaker(auto_commit=False,auto_flush=False,bind=engine)


def get_con():
    try:
        con = engine.connect()
        yield con
    finally:
        con.close()

def get_session():
    try:
        session = SESSION_LOCAL()
        yield session
    finally:
        session.close()

