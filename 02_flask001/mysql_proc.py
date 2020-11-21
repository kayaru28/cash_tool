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

engine = getEngineBattleHistory()
Base=declarative_base(bind=engine)

class BattleHistory(Base):
    __tablename__="battle_history" 
    __table_args__={"autoload": True}

def getSession(engine):
    SessionClass=sessionmaker(engine)
    session=SessionClass()
    return session

def rpsInsert(br:BattleResult ):




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

def recordedBattleResult(name,choice_id,result):
    br=BattleResult()
    br.time_now = datetime.datetime.now()
    br.name = name
    br.choice_id = choice_id
    br.result = result
    rpsInsert(br) 



if __name__ == '__main__':
    recordedBattleResult("SS",1,"win")


