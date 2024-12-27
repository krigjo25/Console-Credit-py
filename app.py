'''
    Title : Credit
    Description :   A program that prompts user for credit card

    Base by : CS50, Problem set 07
    Developed by : @krigjo25
    Date Started : 16.11-23

'''
from time import perf_counter
def main(): 

        #   Prompting the user for a credit card number
        n = input("Credit Card Number : ")
        print(CheckCreditCard(n))

def CheckCreditCard(n):

    #   Reversing the order of the array
    array = [int(i) for i in (n)]

    #   Lambda functions to check the type of credit card
    AMEX = lambda n: True if n[:2] == [3,7] and Luhn(n) else False
    VISA = lambda n: True if n[0] % 4 == 0 and Luhn(n) else False
    MASTERCARD = lambda n: True if n[:2] == [5,5] or n[:2] == [5,1] or n[0] % 2 == 0 and Luhn(n) else False

    #   Ensures that the length of the credit card is valid
    if len(n) > 12 and len(n) < 20:
        
        if VISA(array):
            return "VISA"

        elif AMEX(array):
            return "AMEX"

        elif MASTERCARD(array):
            return "MASTERCARD"
   
    return "INVALID"


def Luhn (n, modulo = 10):

    """
    Luhn Algorithm
    approximate 1 second to run of 1,000,000 secquencial numbers
    3 7 8 2 8 2 2 4 6 3 1 0 0 0 5
    3 7 8 2 8 2 2 4 6 3 1 0 0 0 5
    """
    n = n[::-1]

    num = 0
    
    #   Step 1 : Starting from the rightmost digit, double the value of every second digit
    for i in range(1, len(n), 2):
        number  = n[i] * 2
        
        # Step 2 : if the n is greater than 9 add the digits of the product 
        # Step 3 : Sum the digits of n
        num += ( number // modulo) + (number % modulo) if number > 9 else number
            
            #   Step 3 : Sum the digits of n

    for i in range (0, len(n), 2):
        num += n[i]

    return True if num % modulo == 0 else False

if __name__ == "__main__":
    main()


