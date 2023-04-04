from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL="sqlite:///./todos.db"
# db engine
engine=create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
)
# db session - create an instance of a session
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
# create db model
Base=declarative_base()