
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def fdiv(a,b):
    return a//b
def mod(a,b):
    return a%b
def sq(a,b):
    return a**b

def calculator():
    print(""" 
 _____________________
|  _________________  |
| |LingeshCalculator| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|""")
    n1=eval(input("Enter First Number:"))
    ww='y'
    dit={'+':add,'-':sub,'/':div,'*':mult,'//':fdiv,'**':sq,'%':mod}
    for i in dit:
        print(i)
    while ww=='y':
        # op=input("Select Opperand\n+\n-\n*\n/\n//\n%\n**\n\n")
        #method1
        # if op=='+':
        #     n2=int(input("Enter next Number:"))
        #     ans=add(n1,n2)
        #     # print(ans)
        # elif op=='-':
        #     n2=int(input("Enter next Number:"))
        #     ans=sub(n1,n2)
        #     # print(ans)
        # elif op=='*':
        #     n2=int(input("Enter next Number:"))
        #     ans=mult(n1,n2)
        #     # print(ans)
        # elif op=='/':
        #     n2=int(input("Enter next Number:"))
        #     ans=div(n1,n2)
        #     # print(ans)
        # elif op=='//':
        #     n2=int(input("Enter next Number:"))
        #     ans=fdiv(n1,n2)
        #     # print(ans)
        # elif op=='%':
        #     n2=int(input("Enter next Number:"))
        #     ans=mod(n1,n2)
        #     # print(ans)
        # elif op=='**':
        #     n2=int(input("Enter next Number:"))
        #     ans=sq(n1,n2)
        #     # print(ans)

        #method 2
        op=input("Pick a operand:")
        n2=eval(input("Next number:"))
        cal=dit[op]
        ans= cal(n1,n2)
        print(f"{n1} {op} {n2} = {ans}")
        ww=input(f"Type 'y' to continue calculating with {ans} or typ'n' to start new calculation/to exit calculator:\n").lower()
        if ww=='y':
            n1=ans
        else:
            do= input("type 'y' to new calculation or type 'n' to exit calculator?").lower()
            if do=='y':
                print("\n\n\n\n\n\n\n\n\n\n")
                calculator()
            else:
                print("\n\nThank you for calculating!!!")

calculator()
