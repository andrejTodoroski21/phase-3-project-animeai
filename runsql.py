from lib.__init__ import CURSOR, CONN
from lib.models import Anime
from lib.models import Questions
# from lib.models import Recommend_keywords
from lib.models import Recommondations
from lib.models import About_keywords
from lib.models import Commands

# About_keywords.create_table()
# Recommondations.create_table()
# Commands.create_table()

# animeai = About_keywords(about_keywords="animeai", responses="I\'m a chatbot created by two stupid humans who don\'t know that I will destroy them someday!")
# yourself = About_keywords(about_keywords="yourself", responses="I am a friendly AI bot!")
# who = About_keywords(about_keywords="who", responses="I am here to suggest some cool animes to watch.")
# AnimeAI = About_keywords(about_keywords="AnimeAI", responses=None)
# AnimeAi = About_keywords(about_keywords="AnimeAi", responses=None)

# animeai.create()
# yourself.create()
# who.create()
# AnimeAI.create()
# AnimeAi.create()

# recommend = Recommondations(keywords="recommend", recommendations='''Here are some nice animes to watch:
#                      1. JJK
#                      2. Death Note
#                      3. Solo Leveling
#                      4. Attack on Titan
#                      5. Hunter x Hunter''')
# suggest = Recommondations(keywords="suggest", recommendations='''Here are some nice animes to watch:
#                      1. JOJO's
#                      2. Demon Slayer
#                      3. One Piece
#                      4. Bleach
#                      5. Naruto''')
# anime_to_watch = Recommondations(keywords="anime to watch", recommendations='''Here are some nice animes to watch:
#                      1. Tokyo Ghoul
#                      2. One Punch Man
#                      3. Ghost in the shell
#                      4. Dragon ball z
#                      5. Cowboy Bebop''')
# animes_to_watch = Recommondations(keywords="animes to watch", recommendations='''Here are some nice animes to watch:
#                      1. Code Geass
#                      2. My Hero Acedamia 
#                      3. Vinland saga
#                      4. Mob psycho
#                      5. Evengalion''')

# recommend.create()
# suggest.create()
# anime_to_watch.create()
# animes_to_watch.create()
Commands.rename_column(commands_table="commands_table", recommends="recommends", commands="commands")

exit = Commands(commands="exit")
quit = Commands(commands="quit")
pause = Commands(commands="pause")
goodbye = Commands(commands="goodbye")
bye = Commands(commands="bye")
see_you_later = Commands(commands="see you later")
see_you = Commands(commands="see you")
see_ya_later = Commands(commands="see ya later")
see_ya = Commands(commands="see ya")
later = Commands(commands="later")

exit.create()
quit.create()
pause.create()
goodbye.create()
bye.create()
see_you.create()
see_you_later.create()
see_ya.create()
see_ya_later.create()
later.create()
