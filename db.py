import sqlite3 as sq
import os


def orders_in_work():
    path = os.path.abspath("databse/orders_in_work.sqlite")
    con = sq.connect(path)
    cursor = con.cursor()
    request = """
                CREATE TABLE IF NOT EXISTS orders_in_work_list (
                user_id INTEGER,
                tea TEXT,
                weight INTEGER,
                price INTEGER, 
                status TEXT)
                            """
    cursor.execute(request)
    cursor.close()
    con.close()


def create_user_buy_list():
    path = os.path.abspath("databse/orders.sqlite")
    con = sq.connect(path)
    cursor = con.cursor()
    request = """
            CREATE TABLE IF NOT EXISTS users_buy_list (
            user_id INTEGER,
            tea TEXT,
            weight INTEGER,
            price INTEGER)
                        """
    cursor.execute(request)
    cursor.close()
    con.close()


def tea_bd():
    path = os.path.abspath("databse/tea.sqlite")
    con_tea = sq.connect(path)
    tea_cursor = con_tea.cursor()
    request = """
            CREATE TABLE IF NOT EXISTS tea_list(
            id INTEGER,
            tea TEXT,
            price INTEGER,
            callback TEXT)
                """
    tea_cursor.execute(request)
    tea_cursor.close()
    con_tea.close()


def add_orders_to_db(user_id: int, tea: list):
    con = sq.connect(os.path.abspath("databse/orders.sqlite"))
    cursor = con.cursor()
    req = """INSERT INTO users_buy_list (user_id, tea, weight, price, status) VALUES (?, ?, ?, ?)"""
    for i in tea:
        # Чай продается по цене за 50гр
        data = [user_id, i[0], i[2], i[1] * i[2] // 50]
        cursor.execute(req, data)
        con.commit()
    cursor.close()
    con.close()


def delete_orders_from_db(user_id):
    con = sq.connect(os.path.abspath("databse/orders.sqlite"))
    cursor = con.cursor()
    sql_update_query = """DELETE from users_buy_list where id = ?"""
    cursor.execute(sql_update_query, (user_id,))
    cursor.close()
    con.close()


def get_tea_from_db(tea_name):
    con = sq.connect(os.path.abspath("databse/tea.sqlite"))
    cursor = con.cursor()
    tea_list = cursor.execute(("SELECT * FROM tea_list"))
    cursor.close()
    con.close()
    for i in tea_list:
        if i[2] == tea_name:
            return i


def get_tea_list():
    con = sq.connect(os.path.abspath("databse/tea.sqlite"))
    cursor = con.cursor()
    data = cursor.execute(("SELECT * FROM tea_list"))
    cursor.close()
    con.close()
    return data


def get_tea_name(tea_callback):
    con = sq.connect(os.path.abspath("databse/tea.sqlite"))
    tea_cursor = con.cursor()
    sql_update_query = """SELECT from tea_list where callback = ?"""
    tea_cursor.execute(sql_update_query, (tea_callback,))
    callback = tea_cursor.fetchall()
    con.commit()
    tea_cursor.close()
    con.close()
    return callback


def add_tea_to_bd(tea):
    con = sq.connect(os.path.abspath("databse/tea.sqlite"))
    cursor = con.cursor()
    default_status = 'Заказ принят'
    req = """INSERT INTO tea_list (id, tea, price, callback) VALUES (?, ?, ?, ?)"""
    for i in tea:
        cursor.execute(req, list(i))
        con.commit()
    cursor.close()
    con.close()
