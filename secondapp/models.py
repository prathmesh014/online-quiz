from django.db import models # type: ignore

# Create your models here. 
class Question(models.Model):

    qno=models.IntegerField(primary_key=True)
    qtext=models.CharField(max_length=100)
    answer=models.CharField(max_length=50)
    op1=models.CharField(max_length=50)
    op2=models.CharField(max_length=50)
    op3=models.CharField(max_length=50)
    op4=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)

    def _str_(self) -> str:
         return f"{self.qno , self.qtext, self.answer,self.op1,self.op2}"
    
    class Meta:
         db_table="question"


class UserData(models.Model):

     username=models.CharField(max_length=20,primary_key=True)
     password=models.CharField(max_length=20)
     mobno=models.IntegerField()

     def _str_(self) :
         return f"username is {self.username} and password is {self.password} and mobileno is {self.mobno}"

     class Meta:
          db_table="userdata"



class Result(models.Model):

     username=models.CharField(max_length=20)
     subject=models.CharField(max_length=20)
     score=models.IntegerField()

     class Meta:
          db_table="result"

class Admindata(models.Model):

     username=models.CharField(max_length=20, primary_key =True)    
     password=models.CharField(max_length=20)    

     class Meta:
          db_table="admindata"


                