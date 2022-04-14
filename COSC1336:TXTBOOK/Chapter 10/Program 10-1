import random

# The Coin class simualtes a coin that
# can be flipped.

class Coin:

        # The _ _init_ _ method iinitializes the
        # sideup data attribute with 'Heads'.

        def __init__(self):
            self.sideup = 'Heads'

        # The toss method generates a random number
        # in the range of 0 thru 1. If the number
        # is 0, then sidup is set to 'Heads'.
        # Otherwise, sideup isset to 'Tails'.

        def toss(self):
            if random.randint(0,1) == 0:
                self.sideup = 'Heads'
            else:
                self.sideup = 'Tails'

        # The get-sideup method returns the value
        # referenced by sideup.

        def get_sideup(self):
            return self.sideup
# Program 10-2 
# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = Coin()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin.
    print('I am tossing the coin ...')
    my_coin.toss()

    # Display the side of the ocin that is facing up.
    print('This side is up:', my_coin.get_sideup())

# Call teh main function.
main()