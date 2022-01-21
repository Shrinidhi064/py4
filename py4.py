def datatypes():
    a=int(input("Enter an integer"))
    b=float(input("Enter a floating point number"))
    c=input("Enter a character")
    d=input("Enter a String")
    e1=[]
    for i in range(5):
       e1.append(int(input(f"Enter the element{i+1}")))
    f1=(1,2,3,4)
    print(f1)
    g1={21,4,5}
    print(g1)
    g={"Name":"Shrinidhi","Class":"12th","Place":"Chennai"}
    print("PRINTING DIFFERENT DATA TYPES")
    print("Int type",a)
    print("Float type",b)
    print("Char data type",c)
    print("String datatype",d)
    print("List",e1)
    print("Tuple",f1)
    print("Dictionary",g)
    print("Set",g1)
def getlist():
    lis=[1,2,"Shri","Python",[3,4]]
    for i in range(len(lis)):
        print(f"Element {i+1} is {lis[i]}")
def get():
    p=int(input("Enter the first number"))
    q=int(input("Enter the second number"))
    h=[]
    h.extend([p,q])
    print(h)
    for i in h:
        print(i)
datatypes()
getlist()
get()