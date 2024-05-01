from lib.__init__ import CURSOR, CONN
from lib.models import Questions



Questions.create_table()
queston1 = Questions("sample question")
queston1.create()
