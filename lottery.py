import random

def rand(x,y,z):
    mod=random.choice(x)+random.choice(y)+random.choice(z)
    return ((mod%4)+1)

def choice(a):
    if a==1:
        print("Linear equasions")
    if a==2:
        print("Roots finding")
    if a==3:
        print("Approximations")
    if a==4:
        print("integration")


adir=[3,1,6,6,1,4,5,6,9]
eden=[2,0,6,7,9,6,3,5,1]
guy=[2,0,9,2,9,8,2,7,2]

choice(rand(adir,eden,guy))
