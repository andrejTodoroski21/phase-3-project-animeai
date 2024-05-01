from lib.__init__ import CURSOR, CONN
from lib.models import Anime

Anime.create_table()

jjk = Anime(title="jujustu kaisen")
jjk.create()