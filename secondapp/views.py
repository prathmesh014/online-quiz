from multiprocessing import context
from urllib import request
from django.shortcuts import render   # type: ignore
from django.http import HttpResponse  # type: ignore

from secondapp.models import Admindata, Question, UserData,Result

from rest_framework.decorators import api_view  # type: ignore

from rest_framework.response import Response  # type: ignore

next=0




# Create your views here.

@api_view(['GET'])
def sendData(request):
     return HttpResponse("{'rollno':101,'name':'john'}")

def hello(request):
    return HttpResponse("welcome")

def display(request):
    return render(request,'questions.html')

def addquestion(request):

    Question.objects.create(qno=request.GET["qno"],qtext=request.GET["qtext"],answer=request.GET["answer"],op1=request.GET["op1"],op2=request.GET["op2"],op3=request.GET["op3"],op4=request.GET["op4"],subject=request.GET["subject"])

    return render(request,'questions.html',{'message':'Question Added Successfully'})

def viewquestion(request):
    question = Question.objects.get(qno=request.GET["qno"],subject=request.GET["subject"])

    return render(request,'questions.html',{'question':question})

def deletequestion(request):
    Question.objects.filter(qno=request.GET["qno"],subject=request.GET["subject"]).delete()

    return render(request,'questions.html',{'message':'record deleted'})

def updatequestion(request):
        question=    Question.objects.filter(qno=request.GET["qno"],subject=request.GET["subject"])
        question.update(qtext=request.GET['qtext'],answer=request.GET['answer'],op1=request.GET['op1'],op2=request.GET['op2'],op3=request.GET['op3'],op4=request.GET['op4'])


        return render(request,'questions.html',{'message':'record updated'})

def giveMeRegister(request):
       
       return render(request,"register.html",)



   
def giveMelogin(request):
      
    return render(request,"login.html")

def register(request):
    usernamefrombrowser=request.GET["username"] 
    passfrombrowser=request.GET["password"]
    mobileno=request.GET["mobno"]

    # create method will save given details in database table userdata . it will generate and execute insert query

    UserData.objects.create(username=usernamefrombrowser,password=passfrombrowser,mobno=mobileno)

   # create() will create new row in database table

    #print(connection.queries)

    return render(request,"login.html",{'message':"registration successful . please login now"})
     
def login(request):
    
    usernamefrombrowser=request.GET["username"] #tka
    passfrombrowser=request.GET["password"] # ttdfdf

    request.session["username"]=usernamefrombrowser

    # {username=tka} session dictionary

    try:
        userfromdatabase=UserData.objects.get(username=usernamefrombrowser) # get() will give object from Database
    except:
        return render(request,"login.html",{'message':"Invalid username"})
    
   # print(connection.queries)
    
    # userfromdatabase==> [username=tka  password=tkakiranacademy mobno=12345] UserData class's object is given by get() method

    if userfromdatabase.password == passfrombrowser:
        
        request.session['answers'] = {}
        request.session['score'] = 0
        request.session["qno"]=-1
       
        queryset=Question.objects.filter(subject='python').values()
        listofquestions=list(queryset)
        request.session["listofquestions"]=listofquestions

        return render(request,"subject.html",{'message':"welcome " + usernamefrombrowser})
    
    #serilizable
    
    else:

        return render(request,"login.html",{'message':"Invalid password..",'oldusername':usernamefrombrowser})
     


def nextQuestion(request):

    if 'op' in request.GET:
    
        allanswers=request.session['answers']

        allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

                                         
        print(allanswers)

    allquestions=request.session["listofquestions"]

    questionindex=request.session['qno']
    
    if questionindex<len(allquestions)-1:

        request.session["qno"]=request.session["qno"] + 1
    
        print(f"qno is {request.session['qno']}")

        question=allquestions[request.session["qno"]]

    else:

        return render(request,'questionnavigation.html',{'message':"click on previous",'question':allquestions[len(allquestions)-1]})

    return render(request,'questionnavigation.html',{'question':question})

    # qno=qno+1

def previousQuestion(request):
    if 'op' in request.GET:
    
        allanswers=request.session['answers']

        allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

                                         
        print(allanswers)

    allquestions=request.session.get("listofquestions")

    questionindex=request.session.get('qno')
    
    if questionindex>0:

        request.session["qno"]=request.session["qno"]-1 
    
        print(f"qno is {request.session['qno']}")

        question=allquestions[request.session["qno"]]

    else:

        return render(request,'questionnavigation.html',{'message':"click on previous",'question':allquestions[len(allquestions)-1]})

    return render(request,'questionnavigation.html',{'question':question})

def endexam(request):

    if 'op' in request.GET:
    
        allanswers=request.session['answers']

        allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

                                         
        print(allanswers)


    responses=request.session['answers']
    allanswers2=responses.values()

    for ans in allanswers2:

            print(f' correct answer{ans[2]}')

            if  ans[2]==ans[3]:
                   request.session['score']=request.session['score'] + 1

    finalscore=request.session['score']
    print('f Your score is (finalscore)')   


    usernamefrombrowser=request.session.get('username')
    subjectname=request.session.get('subject')

    Result.objects.create(username=usernamefrombrowser,subject=subjectname,score=finalscore)
    return render(request,'scorecard.html',{'score':finalscore,'responses':allanswers2})

def starttest(request):
    subjectname=request.GET["subject"]
    request.session["subject"]=subjectname

    queryset = Question.objects.filter(subject=subjectname).values()
    listofquestions=list(queryset)
    request.session["listofquestions"]=listofquestions

    return render(request,"questionnavigation.html",{'question':listofquestions[0]})

def adminlogin(request):
     return render(request,"adminlogin.html")
def AdminToLogin(request):
    adminnamefrombrowser=request.GET['adminname']
    passfrombrowser=request.GET['password']

    request.session['adminname']=adminnamefrombrowser

    try:
        adminnamefromdb = Admindata.objects.get(username=adminnamefrombrowser)
    except:
        return render(request, 'adminlogin.html',{'message': 'invalid username'})


    if adminnamefromdb.password == passfrombrowser:

        return render(request,"dashboard.html", {'message':"welcome" + "\t" +  adminnamefrombrowser})

    else:
        return render(request,"adminlogin.html",{"message":"Invalid Credential"})
def dashboard(request):
     return render(request,"dashboard.html")

    
    
    
    
def viewresults(request):
     results =Result.objects.all()
     return render(request,'viewresults.html',{'results':results})
     



     
     


@api_view(['GET'])
def getUser(request,username):
  
    userfromdb=UserData.objects.get(username=username)
    response=Response({'username':userfromdb.username,'password':userfromdb.password,'mobno':userfromdb.mobno})
    return response
@api_view(['GET'])
def getallUser(request):
     queryset=UserData.objects.all().values()

     listofusers= list(queryset)
     return Response(listofusers)

@api_view(['DELETE'])
def deleteUser(request,userfromclient):
    UserData.objects.filter(username=userfromclient).delete()

    return Response({'message':'Record Deleted'})
@api_view(['GET'])
def getallquestions(request):
    allquestions=Question.objects.all().values()
    

    Questionall= list(allquestions)
    return Response(Questionall)
@api_view(['GET'])
def getonlyPYTHONq(request):
    questions=Question.objects.filter(subject="Python")
    questions_py=list(questions.values())
    return Response(questions_py)

@api_view(['GET'])
def getQbySUB(request,subfromuser):    
    que=Question.objects.filter(subject=subfromuser)
    questions=list(que.values())
    return Response(questions)

@api_view(['GET'])
def getQbySUB_Qno(request,subfromuser,qnofromuser):
        ques=Question.objects.filter(subject=subfromuser,qno=qnofromuser)
        questionss=list(ques.values())
        return Response(questionss)

@api_view(['DELETE'])
def deleteQbySUB_Qno(request,subfromuser,qnofromuser):
        ques=Question.objects.filter(subject=subfromuser,qno=qnofromuser).delete()

        return Response({'message':'Record deleted'})
@api_view(['GET'])
def countQNO(request,subjectname):
    question=Question.objects.filter(subject=subjectname)
    questionNO=list(question)
    return Response(len(questionNO))

@api_view(['POST'])
def adduser (request):
    print(request.data)
    userfromclient=request.data

    UserData.objects.create(username=userfromclient['username'],password=userfromclient['password'],mobno=userfromclient['mobno'])

    response=Response(userfromclient)
    return response

@api_view(['PUT'])
def updateUser (request):
    dictionary=request.data
    userfromdb=UserData.objects.get(username=dictionary["username"])
    userfromdb.password=dictionary["password"]
    userfromdb.mobno=dictionary["mobno"]
    userfromdb.save()
    return Response(dictionary)

     
        


