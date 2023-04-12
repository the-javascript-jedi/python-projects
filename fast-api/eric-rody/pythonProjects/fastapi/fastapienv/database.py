from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sqllite connection
# SQLALCHEMY_DATABASE_URL="sqlite:///./todos.db"
# db engine-sqlite
# engine=create_engine(
#     SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
# )

# postgrsql connection
# SQLALCHEMY_DATABASE_URL="postgresql://postgres:admin@localhost/TodoApplicationDatabase"
# engine=create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
#
# # db session - create an instance of a session
# SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

# mysql connection
SQLALCHEMY_DATABASE_URL="mysql+pymysql://root:mysqlroot@127.0.0.1:3306/todoapp"
engine=create_engine(
    SQLALCHEMY_DATABASE_URL
)

# db session - create an instance of a session
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

# create db model
Base=declarative_base()