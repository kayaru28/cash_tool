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
    name = "NA"
    choice_id = 0
    result = ""

def getEngineBattleHistory():
    engine_key = getEngineKey(db_name_rps)
    engine=create_engine(engine_key)

    return engine

def getSession(engine):
    SessionClass=sessionmaker(engine)
    session=SessionClass()
    return session

def rps_insert(br:BattleResult ):

    engine = getEngineBattleHistory()
    Base=declarative_base(bind=engine)
    class BattleHistory(Base):
        __tablename__="battle_history" 
        __table_args__={"autoload": True}

    session = getSession(engine)
    tmpid = getRandomId9()

    insert_battle_history=BattleHistory(
        id          = tmpid,
        time        = br.time_now,
        name        = br.name,
        choice_id   = br.choice_id,
        result      = br.result
    )

    session.add(insert_battle_history)
    session.commit()

    session.close()

br=BattleResult()
br.name = "ss"
br.choice_id = 1
br.result = "win"
rps_insert(br)


