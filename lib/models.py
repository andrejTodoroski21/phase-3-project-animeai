from . import CONN, CURSOR

class Recommondations:
    def __init__(self, title):
        self.title = title
        self.id = id

    @classmethod
    def create_table(self):
        sql = '''CREATE TABLE if not exists anime_recommondations(id INTEGER PRIMARY KEY,
        title TEXT
        );'''
        CURSOR.execute(sql)
        CONN.commit()

    def create(self):
        sql = '''INSERT INTO anime_recommondations(content) VALUES (?)'''
        CURSOR.execute(sql, [self.content])
        CONN .commit()
        last_row_sql = "SELECT * FROM anime_recommondations ORDER BY id DESC LIMIT 1"
        last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
        self.id = last_row_tuple[0]

    @classmethod
    def read_all(cls):
        sql = '''SELECT * FROM anime_recommondations;'''
        all_anime_tuple = CURSOR.execute(sql).fetchall()
        return all_anime_tuple


class Anime:
    def __init__(self, anime):
        self.anime = anime
        self.id = id
    
    @classmethod
    def create_table(self):
        sql = '''CREATE TABLE if not exists animes_table (id INTEGER PRIMARY KEY,
        title TEXT
        );'''
        CURSOR.execute(sql)
        CONN.commit()

    def create(self):
        sql = '''INSERT INTO animes_table(anime) VALUES (?)'''
        CURSOR.execute(sql, [self.content])
        CONN .commit()

        last_row_sql = "SELECT * FROM animes_table ORDER BY id DESC LIMIT 1"
        last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
        self.id = last_row_tuple[0]

class Questions:
    def __init__(self, questions):
        self.questions = questions
        self.id = id

    @classmethod
    def create_table(self):
        sql = '''CREATE TABLE if not exists questions_table (id INTEGER PRIMARY KEY,
        questions TEXT
        );'''
        CURSOR.execute(sql)
        CONN.commit()

    def create(self):
        sql = '''INSERT INTO questions_table (questions) VALUES (?)'''
        CURSOR.execute(sql, [self.questions])
        CONN .commit()

        last_row_sql = "SELECT * FROM questions_table ORDER BY id DESC LIMIT 1"
        last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
        self.id = last_row_tuple[0]

    @classmethod
    def read_all(cls):
        sql = '''SELECT * FROM questions_table;'''

        all_questions_tuple = CURSOR.execute(sql).fetchall()
        return all_questions_tuple