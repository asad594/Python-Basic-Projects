"""Blind Auction CLI Application.

Allows multiple participants to submit secret bids stored in a dictionary mapping,
calculating and declaring the highest bidder at the end of the auction session.
"""

from typing import Dict

LOGO = r'''
                         ___________
                        \         /
                         )_______(
                         |"""""""|_.-._,.---------.,_.-._
                         |       | | |               | | ''-.
                         |       |_| |_             _| |_..-'
                         |_______| '-' `'---------'` '-'
                         )"""""""(
                        /_________\
                      .-------------.
                     /_______________\
'''


def find_highest_bidder(bidding_record: Dict[str, float]) -> None:
    """Evaluate bidding dictionary and display the winner with the highest bid amount.

    Args:
        bidding_record: Mapping of bidder names to bid amounts.
    """
    if not bidding_record:
        print("No bids were placed.")
        return

    winner = max(bidding_record, key=lambda k: bidding_record[k])
    highest_bid = bidding_record[winner]
    print(f"\nThe winner is {winner} with a bid of ${highest_bid:.2f}!")


def main() -> None:
    """Run interactive Blind Auction session."""
    print(LOGO)
    print("Welcome to the Secret Blind Auction Program.")

    bids: Dict[str, float] = {}
    bidding_finished = False

    while not bidding_finished:
        name = input("What is your name?: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue

        try:
            price = float(input("What is your bid?: $"))
            if price <= 0:
                print("Bid must be greater than zero.")
                continue
        except ValueError:
            print("Invalid bid amount! Please enter a valid number.")
            continue

        bids[name] = price

        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
        if should_continue == "no":
            bidding_finished = True
            find_highest_bidder(bids)
        elif should_continue == "yes":
            print("\n" * 50)  # Clear console view between bidders
        else:
            print("Unrecognized response. Ending auction.")
            bidding_finished = True
            find_highest_bidder(bids)


if __name__ == "__main__":
    main()
