
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random

root_user = "root"
root_pass = "Root-0904"
root_host = "localhost"
db_name_rps = "rps"

engine_key_rps = "mysql://"+root_user+":"+root_pass+"@"+root_host+"/" + db_name_rps

engine=create_engine(engine_key_rps)

SessionClass=sessionmaker(engine)
session=SessionClass()

Base=declarative_base(bind=engine)
class BattleHistory(Base):
    __tablename__="battle_history" 
    __table_args__={"autoload": True}


tmpid = int(random.random()*1000000000)
insert_battle_history=BattleHistory(id=tmpid,time="2018-04-10 12:00:00", name="test", choice_id=20,result="win")
session.add(insert_battle_history)
session.commit()

session.close()


