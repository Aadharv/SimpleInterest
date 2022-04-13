def simpleinterest(p,n,r):
    print("principal",p)
    print("The years",n)
    print("rate of interest",r)
    simple=(p*n*r)/100
    print("The simple interest is ",simple)
principal=int(input("What is the principal")) 
years=int(input("The number of years?"))
roi=int(input("What is the rate of interest"))

simpleinterest(principal,years,roi)