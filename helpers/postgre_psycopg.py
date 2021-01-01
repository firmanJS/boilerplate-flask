import psycopg2
import psycopg2.extras
from config import configuration

def connect():
    try:
        conn = psycopg2.connect(host=configuration.postgre_host, port=configuration.postgre_port,
            database=configuration.postgre_db, user=configuration.postgre_user, password=configuration.postgre_password)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    except psycopg2.ProgrammingError as exc:
        print(exc.message)
        conn.rollback()

    except psycopg2.InterfaceError as exc:
        print(exc.message )
        conn = psycopg2.connect(host=configuration.postgre_host, port=configuration.postgre_port,
            database=configuration.postgre_db, user=configuration.postgre_user, password=configuration.postgre_password)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    return conn, cur
