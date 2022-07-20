import random
operator = ['+', '*','-']
error = 0
score = 0
print ("###### WELCOME TO SIMPLE CALCULATION GAME #######")
print ("Rule : +4 for correct answer, -2 for wrong answer")

for i in range (5):
    print("*"*50)
    n1=random.randrange (1,100)
    n2=random.randrange(1,100)
    i=random.randrange(0,3)
    op=operator[i]
    result = 0
    if op=='+':
       result = n1 + n2
    elif op=='-':
        if n1<n2:
            n1,n2=n2,n1
        result = n1 - n2
    elif op=='*':
        result = n1 * n2
    print (n1,op,n2,'=')
    ask =int(input())
    if ask == result:
       score+=4
    else:
        score-=2
print("*"*50)
print("## YOU SCORED : ",score, "##")