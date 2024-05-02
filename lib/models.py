from . import CONN, CURSOR

class Recommondations:
    def __init__(self, recommendations, keywords, id = None):
        self.recommendations = recommendations
        self.id = id
        self.keywords = keywords

    @classmethod
    def create_table(self):
        sql = '''CREATE TABLE if not exists anime_recommondations(id INTEGER PRIMARY KEY,
        recommendations TEXT , keywords TEXT
        );'''
        CURSOR.execute(sql)
        CONN.commit()

    def create(self):
        sql = '''INSERT INTO anime_recommondations(recommendations, keywords) VALUES (?, ?)'''
        CURSOR.execute(sql, [self.recommendations, self.keywords])
        CONN .commit()
        # last_row_sql = "SELECT * FROM anime_recommondations ORDER BY id DESC LIMIT 1"
        # last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
        # self.id = last_row_tuple[0]

    @classmethod
    def read_all(cls):
        sql = '''SELECT * FROM anime_recommondations;'''
        all_anime_tuple = CURSOR.execute(sql).fetchall()
        return all_anime_tuple

    def retreive_keywords(self):
        sql = '''SELECT keywords FROM anime_recommondations;'''
        all_keywords_tuples =  cursor.execute(sql).fetchall()
        all_keywords = [keyword[0] for keyword in all_keywords_tuples]

        return all_keywords

    def retreive_recommondations(self):
        sql = '''SELECT recommendations FROM anime_recommondations;'''
        all_recommendations_tuples =  cursor.execute(sql).fetchall()
        all_recommendations = [recommendation[0] for recommendation in all_recommendations_tuples]

        return all_recommendations



class Anime:


    all_animes = []
    all_art = []

    def __init__(self, title, ascii_art, id = None):
        self.title = title
        self.id = id
        self.ascii_art = ascii_art
    
    @classmethod
    def create_table(self):
        sql = '''CREATE TABLE if not exists animes_table (id INTEGER PRIMARY KEY,
        title TEXT, ascii_art TEXT
        );'''
        CURSOR.execute(sql)
        CONN.commit()

    def create(self):
        sql = '''INSERT INTO animes_table(title, ascii_art) VALUES (?, ?)'''
        CURSOR.execute(sql, [self.title, self.ascii_art])
        CONN .commit()

        # last_row_sql = "SELECT * FROM animes_table ORDER BY id DESC LIMIT 1"
        # last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
        # self.id = last_row_tuple[0]
    @classmethod
    def read_all(cls):
        sql = '''SELECT title FROM animes_table;'''

        all_animes_tuples = CURSOR.execute(sql).fetchall()
        cls.all_animes = [ anime[0] for anime in all_animes_tuples]
        return cls.all_animes
    
    @classmethod
    def read_all_art(cls):
        sql = '''SELECT ascii_art FROM animes_table;'''

        all_animes_art_tuples = CURSOR.execute(sql).fetchall()
        print(all_animes_art_tuples)
        cls.all_art = [ art[0] for art in all_animes_art_tuples]
        return cls.all_art


    @classmethod
    def add_column(cls):
        sql = '''ALTER TABLE animes_table 
               ADD COLUMN ascii_art TEXT;'''
        CURSOR.execute(sql)
        CONN.commit() 


class Questions:

    all_questions = []

    def __init__(self, questions, id = None):
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

        # last_row_sql = "SELECT * FROM questions_table ORDER BY id DESC LIMIT 1"
        # last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
        # self.id = last_row_tuple[0]


    @classmethod
    def read_all(cls):
        sql = '''SELECT * FROM questions_table;'''

        all_questions_tuples = CURSOR.execute(sql).fetchall()
        cls.all_questions = [ question[1] for question in all_questions_tuples]
        return cls.all_questions

    @classmethod
    def update_id(cls, id, id1):
        sql = '''UPDATE questions_table SET id = ? WHERE id = ?''' 
        CURSOR.execute(sql, [id, id1])
        CONN.commit()

class About_keywords:

    all_about_keywords = []

    all_responses = []


    def __init__(self, about_keywords, responses, id = None):
        self.id = id
        self.about_keywords = about_keywords
        self.responses = responses

    @classmethod
    def create_table(self):
        sql = '''CREATE TABLE if not exists about_commands_table (id INTEGER PRIMARY KEY,
        about_keywords TEXT, responses TEXT);'''
        CURSOR.execute(sql)
        CONN.commit()

    def create(self):
        sql = '''INSERT INTO about_commands_table(about_keywords, responses) VALUES (?,?)'''
        CURSOR.execute(sql, [self.about_keywords, self.responses])
        CONN .commit()

    @classmethod
    def retreive_about_keywords(cls):
        sql = '''SELECT about_keywords FROM about_commands_table;'''
        all_about_keywords_tuples =  CURSOR.execute(sql).fetchall()
        cls.all_about_keywords = [about_keyword[0] for about_keyword in all_about_keywords_tuples]

        return cls.all_about_keywords
    
    @classmethod
    def retreive_recommondations(cls):
        sql = '''SELECT responses FROM about_commands_table;'''
        all_responses_tuples =  CURSOR.execute(sql).fetchall()
        cls.all_responses = [response[0] for response in all_responses_tuples]

        return cls.all_responses

class Commands:

    all_commands = []

    def __init__(self, commands, id = None):
        self.id = id
        self.commands = commands

    @classmethod
    def create_table(self):
        sql = '''CREATE TABLE if not exists commands_table (id INTEGER PRIMARY KEY,
        commands TEXT);'''
        CURSOR.execute(sql)
        CONN.commit()

    def create(self):
        sql = '''INSERT INTO commands_table(commands) VALUES (?)'''
        CURSOR.execute(sql, [self.commands])
        CONN .commit()

    def rename_column(commands_table, recommends, commands):
        # Construct the SQL query to rename the column
        sql = '''ALTER TABLE commands_table RENAME COLUMN recommends TO commands;'''
        
        CURSOR.execute(sql)
        CONN.commit()    

    @classmethod
    def read_all(cls):
        sql = '''SELECT * FROM commands_table;'''

        all_commands_tuples = CURSOR.execute(sql).fetchall()
        cls.all_commands = [ command[1] for command in all_commands_tuples]
        return cls.all_commands

