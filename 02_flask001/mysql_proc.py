
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine=create_engine("mysql://root:Root-0904@localhost/rps")

SessionClass=sessionmaker(engine)
session=SessionClass()

Base=declarative_base(bind=engine)
class BattleHistory(Base):
    __tablename__="battle_history" 
    __table_args__={"autoload": True}



insert_battle_history=BattleHistory(id=1,time="2018-04-10 12:00:00", name="test", choice_id=20,result="win")
session.add(insert_battle_history)
session.commit()

session.close()


