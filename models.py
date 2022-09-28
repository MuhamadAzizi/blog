import mysql.connector


def start_connection():
    cnx = mysql.connector.connect(
        user='root', password='',
        host='localhost', database='blog')
    return cnx


def get_all_users():
    query = ('SELECT * FROM users')

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)

    result = []
    for id, name, email_address, password, user_level in cursor:
        row = []
        row.append(id)
        row.append(name)
        row.append(email_address)
        row.append(password)
        row.append(list(user_level)[0])
        result.append(row)

    cursor.close()
    cnx.close()
    return result


def login_auth(email_address, password):
    query = (
        f"SELECT * FROM users WHERE email_address = '{email_address}' AND password = '{password}'")

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)

    result = {}
    for id, name, email_address, password, user_level in cursor:
        result['id'] = id
        result['name'] = name
        result['email_address'] = email_address
        result['password'] = password
        result['user_level'] = user_level

    cursor.close()
    cnx.close()
    return result
