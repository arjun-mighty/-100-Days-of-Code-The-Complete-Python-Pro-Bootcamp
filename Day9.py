import os
os.system('clear')
from Day9art import logo
print(logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record: #looping through dictionary
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner = bidder
    print(f"The Winner is {winner},with a bid of${highest_bid}")
        
    

while not  bidding_finished:
    name = input("What is your name ? : ")
    price= int(input("What is your bid?: $"))
    bids[name] = price
    should_continue=input("Are there any other bidders? type 'yes' or 'no' ")
    if should_continue =="no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue =="yes":
        os.system('clear')
    
    
    