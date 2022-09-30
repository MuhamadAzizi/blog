import mysql.connector


def start_connection():
    cnx = mysql.connector.connect(
        user='root', password='',
        host='localhost', database='blog')
    return cnx


def add_article(title, slug, labels_id, thumbnail, date_posted, content, users_id):
    query = (
        f"INSERT INTO articles(title, slug, labels_id, thumbnail, date_posted, content, users_id) VALUES('{title}', '{slug}', '{labels_id}', '{thumbnail}', '{date_posted}', '{content}', '{users_id}')")

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def delete_article(id):
    query = (f"DELETE FROM articles WHERE id = {id}")

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def get_all_articles():
    query = (
        'SELECT articles.id, articles.title, articles.slug, labels.label, articles.thumbnail, articles.date_posted, articles.content, users.name FROM articles INNER JOIN labels ON articles.labels_id = labels.id INNER JOIN users ON articles.users_id = users.id')

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)

    result = []
    for id, title, slug, label, thumbnail, date_posted, content, name in cursor:
        result.append({
            'id': id,
            'title': title,
            'slug': slug,
            'label': label,
            'thumbnail': thumbnail,
            'date_posted': date_posted,
            'content': content,
            'name': name
        })

    cursor.close()
    cnx.close()
    return result


def get_article_by_id(id):
    query = (f"SELECT * FROM articles WHERE id = {id}")

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)

    result = {}
    for id, title, slug, labels_id, thumbnail, date_posted, content, users_id in cursor:
        result['id'] = id
        result['title'] = title
        result['slug'] = slug
        result['labels_id'] = labels_id
        result['thumbnail'] = thumbnail
        result['date_posted'] = date_posted
        result['content'] = content
        result['users_id'] = users_id

    cursor.close()
    cnx.close()
    return result


def get_all_labels():
    query = ('SELECT * FROM labels')

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)

    result = []
    for id, label in cursor:
        result.append({
            'id': id,
            'label': label
        })

    cursor.close()
    cnx.close()
    return result


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


def get_user_by_id(id):
    query = (
        f"SELECT * FROM users WHERE id = {id}")

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)

    result = {}
    for id, name, email_address, password, user_level in cursor:
        result['id'] = id
        result['name'] = name
        result['email_address'] = email_address
        result['password'] = password
        result['user_level'] = list(user_level)[0]

    cursor.close()
    cnx.close()
    return result

    result = {}
    for id, name, email_address, password, user_level in cursor:
        result['id'] = id
        result['name'] = name
        result['email_address'] = email_address
        result['password'] = password
        result['user_level'] = list(user_level)[0]

    cursor.close()
    cnx.close()
    return result


def update_user(id, name, email_address, password, user_level):
    query = (
        f"UPDATE users SET name = '{name}', email_address = '{email_address}', password = MD5('{password}'), user_level = '{user_level}' WHERE id = {id}")

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def add_user(name, email_address, password, user_level):
    query = (
        f"INSERT INTO users(name, email_address, password, user_level) VALUES('{name}', '{email_address}', MD5('{password}'), '{user_level}')")

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def delete_user(id):
    query = (
        f"DELETE FROM users WHERE id = {id}")

    cnx = start_connection()
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


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
        result['user_level'] = list(user_level)[0]

    cursor.close()
    cnx.close()
    return result
