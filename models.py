import mysql.connector

cnx = mysql.connector.connect(
    user='root', password='',
    host='localhost', database='blog')
cursor = cnx.cursor()

def get_all_users():
    query = ('SELECT * FROM users')
    cursor.query(query)

    result = {
        'id': [],
        'name': [],
        'email_address': [],
        'password': [],
        'user_level': []
    }
    for id, name, email_address, password, user_level in cursor:
        result['id'].append(id)
        result['name'].append(name)
        result['email_address'].append(email_address)
        result['password'].append(password)
        result['user_level'].append(user_level)

    cursor.close()
    return result

cnx.close()