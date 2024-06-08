import sqlite3


class SQLiteConnector:
    def __init__(self, path:str):
        self.__path = path
        self.__connection = sqlite3.connect(self.__path)
        self.__cursor = self.__connection.cursor()

    @property
    def cursor(self):
        return self.__cursor

    def exec(self, query:str):
        return  self.__cursor.execute(query)

    def __del__(self):
        self.__cursor.close()
        self.__connection.close()


def create_table_user():
    con = SQLiteConnector('auth_db.db')

    con.cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id int primary_key,
    username text unique,
    password text,
    email text unique
    );
    """)

    del con


if __name__ == '__main__':
    # create_table_user()

    con = SQLiteConnector('auth_db.db')



    del con
