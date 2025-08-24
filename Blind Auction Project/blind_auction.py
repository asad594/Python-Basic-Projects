logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


def highest_bidder(bidding_dictioanry):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictioanry:
        bidd_amount = bidding_dictioanry[bidder]
        if bidd_amount > highest_bid:
            highest_bid = bidd_amount
            winner = bidder
    print(f"The winner is {winner} with a highest bidd ${highest_bid}")


should_continue = True
blind_auction = {}
while should_continue:
    name = input("What is your name : ")
    price = int(input("What is your bid : $"))
    blind_auction[name] = price
    restart = input("Are there any other bidders ? Type 'yes' or 'no' : \n").lower()
    if restart == "yes":
        print("\n" * 20)
    elif restart == "no":
        should_continue = False
        highest_bidder(blind_auction)
        print("Good Bye")
    else:
        print("Invalid Input")
        should_continue = False

