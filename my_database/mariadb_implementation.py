from .database import Database
import mysql.connector

class MariaDB(Database):
    def __init__(self, host, user, password, database, debug: bool=False):
        self.host: str = host
        self.user: str = user
        self.password: str = password
        self.database: str = database
        self.connection = None
        self.cursor = None
        self.debug = debug

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, table_name: str, columns: list[str], rows: list[list[str]]):
        values = []
        for row in rows:
            values.append(f'({",".join([value for value in row])})')
        
        
        query = f'INSERT INTO {table_name} ({",".join(columns)}) VALUES {",".join(values)};'

        if self.debug:
            print(query)
            
        self.cursor.execute(query)
        

    def select(self, table_name: str, columns: list[str], where: str = ''):
        query = f'SELECT {"("+",".join(columns)+")" if columns[0] != "*" else "*"} FROM {table_name}'

        if where:
            query += f'WHERE {where}'

        query += ';'

        if self.debug:
            print(query)
        
        self.cursor.execute(query)
            
        return self.cursor.fetchall()
        
        
    def delete(self, table_name: str, where: str):
        query = f'DELETE FROM {table_name} WHERE {where};'
        
        if self.debug:
            print(query)
        
        self.cursor.execute(query)

        
    def update(self, table_name: str, assignements: list[str], where: str):
        query = f'UPDATE {table_name} SET {",".join(assignements)} WHERE {where}'
        
        if self.debug:
            print(query)
        
        self.cursor.execute(query)
        