from django.db import models

# Create your models here.
class Group(models.Model):
    QunNum = models.IntegerField()
    MastQQ = models.IntegerField()
    CreateDate = models.CharField(max_length=10)
    Title = models.CharField(max_length=22)
    Class = models.CharField(max_length=38)
    QunText = models.CharField(max_length=80)

    def __str__(self):
        return str({
            'QunNum': self.QunNum,
            'MastQQ':self.MastQQ,
            'CreateDate':self.CreateDate,
            'Title':self.Title,
            'Class':self.Class,
            'QunText':self.QunText
        })

class Account(models.Model):
    QQNum = models.IntegerField()
    Nick = models.CharField(max_length=80)
    Age = models.IntegerField()
    Gender = models.IntegerField()
    Auth = models.IntegerField()
    QunNum = models.IntegerField()

    def __str__(self):
        return str({
            'QQNum':self.QQNum,
            'Nick':self.Nick,
            'Age':self.Age,
            'Gender':self.Gender,
            'Auth':self.Auth,
            'QunNum':self.QunNum

        })