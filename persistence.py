import bcrypt

import database_common

@database_common.connection_handler
def get_data_from_public_boards(cursor):
    cursor.execute("""
        SELECT * FROM boards
        WHERE owner = 'public';
    """)
    all_boards = cursor.fetchall()
    return all_boards


@database_common.connection_handler
def get_data_from_user_boards(cursor, username):
    cursor.execute("""
        SELECT * FROM boards
        WHERE owner = %(username)s;
    """,
        {'username': username})
    all_boards = cursor.fetchall()
    return all_boards


def _get_public_boards(data_type, force):
    """
    Reads defined type of data from file or cache
    :param data_type: key where the data is stored in cache

    :param force: if set to True, cache will be ignored
    :return: OrderedDict
    """
    if force or data_type not in _cache:
        _cache[data_type] = get_data_from_public_boards()
    return _cache[data_type]


def _get_user_boards(data_type, force, username):
    """
    Reads defined type of data from file or cache
    :param data_type: key where the data is stored in cache

    :param force: if set to True, cache will be ignored
    :return: OrderedDict
    """
    username = username

    if force or data_type not in _cache:
        _cache[data_type] = get_data_from_user_boards(username)
    return _cache[data_type]


def clear_cache():
    for k in list(_cache.keys()):
        _cache.pop(k)


# def get_statuses(force=False):
#     return _get_data('statuses', statuses, force)


def get_public_boards(force=False):
    return _get_public_boards('boards', force)


def get_user_boards(force=False):
    return _get_user_boards('boards', force)


# def get_cards(force=False):
#     return _get_data('cards', cards, force)


#password hashing:

def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


@database_common.connection_handler
def login(cursor, username):
    cursor.execute("""
        SELECT password FROM users
        WHERE username = %(username)s;
        """,
         {'username': username})
    password = cursor.fetchone()
    return password


@database_common.connection_handler
def add_user(cursor, data):
    cursor.execute("""
        INSERT INTO users(username, password)
        VALUES (%s, %s);
    """,
       (data['username'],
        data['password']))



# import csv
#
# STATUSES_FILE = './data/statuses.csv'
# BOARDS_FILE = './data/boards.csv'
# CARDS_FILE = './data/cards.csv'
#
_cache = {}  # We store cached data in this dict to avoid multiple file readings
#
#
# def _read_csv(file_name):
#     """
#     Reads content of a .csv file
#     :param file_name: relative path to data file
#     :return: OrderedDict
#     """
#     with open(file_name) as boards:
#         rows = csv.DictReader(boards, delimiter=',', quotechar='"')
#         formatted_data = []
#         for row in rows:
#             formatted_data.append(dict(row))
#         return formatted_data
#



