import random
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

root_user = "root"
root_pass = "Root-0904"
root_host = "localhost"
db_name_rps = "rps"



def getEngineKey(db_name):
    return "mysql://"+root_user+":"+root_pass+"@"+root_host+"/" + db_name

def getRandomId9():
    return int(random.random()*1000000000)

class BattleResult():
    time_now = datetime.datetime.now()

def rps_insert():

    engine_key = getEngineKey(db_name_rps)
    engine=create_engine(engine_key)
    Base=declarative_base(bind=engine)
    class BattleHistory(Base):
        __tablename__="battle_history" 
        __table_args__={"autoload": True}

    SessionClass=sessionmaker(engine)
    session=SessionClass()

    tmpid = getRandomId9()
    insert_battle_history=BattleHistory(id=tmpid,time=datetime.datetime.now(), name="test", choice_id=20,result="win")

    session.add(insert_battle_history)
    session.commit()

    session.close()

rps_insert()


