from PyQt5 import QtSql
from PyQt5.QtSql import *


class Database:
    is_instantiated = False

    def __init__(self):
        if not Database.is_instantiated:
            print("Database has been instantiated!")
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName('C:/Users/jsearl/OneDrive - Capstan Corporation/Desktop/Yard Manage/Pipe Spool Manager py/Pipe_Master/spool_DB.db')
            self.db.open()
            Database.is_instantiated = True
        else:
            print("Has already been created")
