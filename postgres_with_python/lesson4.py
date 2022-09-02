#importing liberaries
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

 #column names as arguements
columns = [
    'phone_number',
    'first_name',
    'last_name',
    'age',
    'gender']

#loading the random data list
data = pd.read_csv('random list.csv', names=columns)

#using sqlalchemy.create_engine object
engine = create_engine("postgresql+psycopg2://postgres:zoway005?@localhost:4199/demo_db", pool_recycle = -1)

#saving data from dataframe to postgres table
data.to_sql("random list", engine, index = True)
