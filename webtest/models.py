from django.db import models

# Create your models here.
import mongoengine
class Student(mongoengine.Document):
    name = mongoengine.StringField(max_length=32)
    age = mongoengine.IntField(defaul=0)
    _id = mongoengine.StringField(max_length=32)
class listtwot(mongoengine.Document):
    _id = mongoengine.StringField(max_length=32)
    city = mongoengine.StringField(max_length=12)
    cname = mongoengine.StringField(max_length=12)
    curl = mongoengine.StringField(max_length=64)
    jobType = mongoengine.StringField(max_length=32)
    title = mongoengine.StringField(max_length=12)
    b_type = mongoengine.StringField(max_length=32)
    study = mongoengine.StringField(max_length=12)
    workingExp = mongoengine.StringField(max_length=32)
    updateDate = mongoengine.StringField(max_length=32)
    salary = mongoengine.StringField(max_length=12)
    welfare = mongoengine.ListField(max_length=32)
    positionURL = mongoengine.StringField(max_length=32)
    jobTypeName = mongoengine.StringField(max_length=32)
    jobName = mongoengine.StringField(max_length=32)
    posdetail = mongoengine.StringField()

class citycount(mongoengine.Document):
    _id = mongoengine.StringField(max_length=32)
    cityname = mongoengine.StringField(max_length=12)
    type = mongoengine.StringField(max_length=12)
    shuliang =  mongoengine.StringField(max_length=12)

