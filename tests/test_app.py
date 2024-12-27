from app import CheckCreditCard, Luhn

import time
def test_amex():

    #   Ensuring the card is AMEX
    amex1 = "378282246310005"
    amex2 = "371449635398431"
    
    assert CheckCreditCard(amex1) == "AMEX"
    assert CheckCreditCard(amex2) == "AMEX"

def test_visa():
    #   Ensuring the card is VISA
    visa1 = "4222222222222"
    visa2 = "4111111111111111"

    assert CheckCreditCard(visa1) == "VISA"
    assert CheckCreditCard(visa2) == "VISA"

def test_mastercard():
    #   Ensuring the card is MASTERCARD
    master = "5105105105105100"
    master1 = "5555555555554444"

    assert CheckCreditCard(master) == "MASTERCARD"
    assert CheckCreditCard(master1) == "MASTERCARD"

def test_invalid():

    #   Ensuring the card is INVALID
    invalid = "1234567890"
    invalid1 = "4062901840"
    invalid2 = "4222222222223"
    invalid3 = "369421438430814"
    invalid4 = "5673598276138003"
    invalid5 = "4111111111111113"
    

    assert CheckCreditCard(invalid) == "INVALID"
    assert CheckCreditCard(invalid1) == "INVALID"
    assert CheckCreditCard(invalid2) == "INVALID"
    assert CheckCreditCard(invalid3) == "INVALID" # This test case is AMEX
    assert CheckCreditCard(invalid4) == "INVALID" # This test case is MASTER CARD
    assert CheckCreditCard(invalid5) == "INVALID"

    
def test_performance():
    #   Ensuring the performance of the function
    
    start = time.perf_counter()
    
    for i in range(1000000):
        Luhn([3782822463100058342])

    end = time.perf_counter()
    print(f"Time taken : {end - start}s")

    start = time.time()
    CheckCreditCard("4111111111111111")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("5105105105105100")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("1234567890")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("4062901840")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("4222222222223")
    end = time.time()

    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("369421438430814")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("5673598276138003")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("4111111111111113")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("378282246310005")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("4111111111111111")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("5105105105105100")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("1234567890")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
    CheckCreditCard("4062901840")
    end = time.time()
    assert end - start < 1.0
    start = time.time()
