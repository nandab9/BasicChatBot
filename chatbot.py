def greetings():
    print("hello ! , welcome to Destiny career. ")
    print("here you can find all the possibilities and ways by studying the intermediate in the MPC")
    return 

def what_you_have_choices():
    print("May I know your name.")
    name=input()
    print(name+" please choose one what you need.")
    print()
    choice_view=['1.Entrance Exams','2.B.E/Btech','3.B.Arch','4.B.sc','5.Integrated M.sc.','6.B.L','7.Jobs']

    for i in choice_view:
        print(i)
    print()
    print('please enter you option in the numericals.....')
    return 

def bot():
    greetings()
    what_you_have_choices()
    choosen_option=int(input())
    if choosen_option==1:
        Entrance_exams()
    elif choosen_option==2:
        Btech()
    elif choosen_option==3:
        Arch()
    elif choosen_option==4:
        Bsc()
    elif choosen_option==5:
        integrated_Msc()
    elif choosen_option==6:
        Bl()
    else:
        Jobs()

    return
def Entrance_exams():
    print("IIT-JEE,BitSat,EAMCET , these are exams you can go with for futher studies.")
    return

def  Btech():
    print("Normally it is a four ye B.l()ars degree.")
    print("most of the students will choose thes groups like ")
    groups=['CSE','ECE','MECH','CIVIL','EEE','IT']
    for i in groups:
        print(i)
    print('..........nextly after this u can do job or do further high studies')
    return 

def Arch():
    print('this is a arcitect degree and it is very popular in abrode and you can approch this qualifying in the B.Arch exam.')
    return 

def Bsc():
    print('this is a 3 years degree ')
    print('the groups  are ...')
    sub=['maths,chemistry,physics','com.science,maths,physics','maths,physics,electronics','maths,statics,com.sciencs']
    for i in sub:
        print(i)
    return 

def integrated_Msc():
    print('It is a 5 years degree ')
    print('here the btech and mtech are done n five years and the students posess jobs or go on with Ph.D .')
    return

def  Bl():
    print('with B.L you can go with M.L and then Ph.D')
    return

def Jobs():
    print('please tell us jobs via B.Tech or B.Sc...')
    print('1.B.Tech, 2. B.Sc')
    job_choosen=int(input())
    if job_choosen==1:
        print("Civils,Groups,IES,IFS,Defence,Railways,Banks,AEE,PSUs,IT,Pharma,cementy,Automobile,Real Estate....")
    else:
        print("Civils,Groups,Defence,IFS,Banks,Computers,Retail,Mediua,Entertainment...")
    return



bot()