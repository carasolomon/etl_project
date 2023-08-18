import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, insert

# Read CSV file and returns DataFrame
def extract(file_path):
    data = pd.read_csv(file_path)
    return data

# Cleans data
def transform(data):
    data['name'].fillna('Unknown', inplace=True)
    return data

# Loads data into database
def load(data, database_path):
    engine = create_engine(f'sqlite:///{database_path}')
    metadata = MetaData()

    # Define the table
    users = Table('users', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('age', Integer),
    )

    # Create the table
    metadata.create_all(engine)

    # Insert the data
    conn = engine.connect()
    for index, row in data.iterrows():
        ins = insert(users).values(id=row['id'], name=row['name'], age=row['age'])
        conn.execute(ins)

# Execute ETL process
def etl(file_path, database_path):
    data = extract(file_path)
    data = transform(data)
    load(data, database_path)

# Usage
if __name__ == '__main__':
    etl('data.csv', 'database.db')
