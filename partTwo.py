import math  

def main():
    A = float(input('Enter length A > '))
    B = float(input('Enter length B > '))
    print (pythag(A,B))

def pythag(A,B):
    C = ((A**2) + (B**2))
    return C

main()
