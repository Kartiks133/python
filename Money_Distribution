import random

Bank_amt=200000

hundred_notes=(0.1*Bank_amt)//100
two_hundred_notes=(0.2*Bank_amt)//200
five_hundred_notes=(0.7*Bank_amt)//500

def withdraw(with_amt):
    global Bank_amt,hundred_notes,two_hundred_notes,five_hundred_notes

    if(with_amt>Bank_amt):
        return "Insufficient Funds!"
    
    withdrawl_amt=with_amt
    notes_500=notes_100=notes_200=0

    if(five_hundred_notes>0):
        notes_500=min(with_amt//500,five_hundred_notes)
        with_amt-=notes_500*500

    if(two_hundred_notes>0 and with_amt>0):
        notes_200=min(with_amt//200,two_hundred_notes)
        with_amt-=notes_200*200

    if(hundred_notes>0 and with_amt>0):
        notes_100=min(with_amt//100,hundred_notes)
        with_amt-=notes_100*100

    if(with_amt>0):
        return "Unable to dispense exact amount. Transaction Failed!"

    Bank_amt-=withdrawl_amt
    five_hundred_notes-=notes_500
    two_hundred_notes-=notes_200
    hundred_notes-=notes_100

    return{
        "Amount Withrawn": withdrawl_amt,
        "500 notes": notes_500,
        "200 notes": notes_200,
        "100 notes": notes_100,
        "Updated bank amount": Bank_amt
    }

def card_check(card_name):
    if(card_name.lower()!="sbi"):
        raise ValueError("ATM card does not belong to SBI.")
    
random_message=[
    "This card is not supported.Please check bank details.",
    "Sorry, we only support SBI cards for transactions",
    "Please use a valid SBI card for withdrawls"
]
    

for customer in range(1,11):
    print(f"\nCustomer{customer}:")
    
    bank_name=input("Enter ATM card issuer")
    try:
        card_check(bank_name)

        withdrawl_amt=int(input("Enter amount to be withdrawn for Customer{customer}"))
        if(withdrawl_amt>20000):
            print("Maximum Limit per user reached")
            continue
        result=withdraw(withdrawl_amt)

        if isinstance(result,dict):
            print("fWithdrawl successful:{result}")
        else:
            print(result)
    except ValueError as e:
        print(random.choice(random_message))
