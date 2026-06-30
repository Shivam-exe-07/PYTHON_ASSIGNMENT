def CheckDivisible(No):
    if((No%3==0 and No%5==0)):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")
        
def main():
    print("Enter the number :")
    Value = int(input())
    
    CheckDivisible(Value)
    
if __name__ == "__main__":
    main()
