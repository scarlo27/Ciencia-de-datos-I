from sqlalchemy import create_engine

def get_mysql_engine(user, password, host, port, database):
   
    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    return engine