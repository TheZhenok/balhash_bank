# Python
from decouple import config
import datetime

# Local
from database.core import Connection
from database.models.users import User


my_connection: Connection = Connection(
    host=config('DB_HOST', str),
    port=config('DB_PORT', int),
    user=config('DB_USER', str),
    password=config('DB_PASSWORD', str),
    dbname=config('DB_NAME', str)
)

if __name__ == '__main__':
    print(
        User.get(conn=my_connection.conn, id=7)
    )
    