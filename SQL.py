import sqlite3
from random import randint


global db
global sql
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

db.commit()


def reg():
    user_login = input('Login:')
    user_password = input('Password:')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)",(user_login, user_password, 0))
        db.commit()

        print('Registred !')
    else:
        print('This data is already passed!')

        for value in sql.execute("SELECT * FROM users"):
            print(value)

def delete_db():
    sql.execute(f'DELETE FROM users WHERE login = "{user_login}"')
    db.commit()

    print('Data removed!')

def casino():
    global user_login
    user_login = input('Log in: ')
    number = randint(1,3)

    #for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
       # balance = i[0]
    #sql.execute(f'SELECT cash FROM users WHERE login = "{user_login}"')
    #balance = sql.fetchone()

    sql.execute(f'SELECT login FROM users WHERE login= "{user_login}"')
    if sql.fetchone() is None:
        print("That login isn't created. Try ty reg it again")
        reg()

    if number == 1:
        sql.execute(f'UPDATE users SET cash = cash + 1000 WHERE login = "{user_login}"')
        db.commit()
    else:
        print('Officially u suck')
        delete_db()
def enter():
    for i in sql.execute('SELECT login,cash FROM users'):
        print(i)


if __name__ == "__main__":
    casino()
    enter()