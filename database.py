from peewee import *
#import datetime

db = SqliteDatabase('data.db')


class BaseModel(Model):
    class Meta:
        database = db


class Visitors(BaseModel):
    id = CharField(null=True)
    visitors_count = IntegerField(null=True)
    time = DateTimeField(null=True) 

class Visitors_Daily(BaseModel):
    id = CharField(null=True)
    visitors_count = IntegerField(null=True)
    time = DateTimeField(null=True) 

db.connect()
db.create_tables([Visitors,Visitors_Daily], safe=True)

""" save = Visitors.create(id="all", visitors_count=1,time=datetime.datetime.now())
save.save()

save = Visitors_Daily.create(id="daily", visitors_count=1,time=datetime.datetime.now())
save.save() """