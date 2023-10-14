# my_database/__init__.py

from .database import Database
from .mysql_implementation import MySQL
from .mariadb_implementation import MariaDB

__all__ = ['Database', 'MySQL', 'MariaDB']