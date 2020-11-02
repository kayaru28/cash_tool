
#import MySQLdb 

#conn = MySQLdb.connect(
#user='root',
#passwd='Root-0904',
#host='localhost',
#db='rps')

#conn.close

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

engine=create_engine("mysql://root:Root-0904@localhost/rps")


#SessionClass=sessionmaker(engine)
#session=SessionClass()

m = MetaData()
m.reflect(engine)
for table in m.tables.values():
    print(table.name)