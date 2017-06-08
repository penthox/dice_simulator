from random import randint

def exit_program():
    print "Wrong Number!"
    exit()

def calculate():
    cur_money = int(float(START_MONEY))
    cur_bet = float(BET)
    for counter in range(1,int(float(ROUNDS))+1):
        if cur_money >= cur_bet:
            cur_money -= cur_bet
            roll = randint(0,100)
            if roll < int(float(CHANCE)):
                cur_money += cur_bet*float(PAYOUT_ADDS)
                cur_bet = float(BET)
            else:
                cur_bet = cur_bet*float(LOOSE_IN)
        else:
            print "Stopped after",counter,"rounds, because your current bet(",cur_bet,") is exceeding your money(",cur_money,")"
            break
    print "That's what you would have after that:",cur_money

print "Welcome to the Dice-Simulator!"
print "How much money do you have?"
START_MONEY = raw_input("> ")
if START_MONEY.isdigit() is False:
    exit_program()
print "How high is the Winning-Chance? (10-90)"
CHANCE = raw_input("> ")
if CHANCE.isdigit() is False or CHANCE > "90" or CHANCE < "10":
    exit_program()
print "How much is the payout multiplier at this chance?"
PAYOUT_ADDS = raw_input("> ")
if PAYOUT_ADDS.isdigit() is False:
    exit_program()
print "How much do you want to bet every round?"
BET = raw_input("> ")
if BET.isdigit() is False:
    exit_program()
print "How many times do you want to increase your bet if you loose?"
LOOSE_IN = raw_input("> ")
if LOOSE_IN.isdigit() is False:
    exit_program()
print "How many rounds do you want to go?"
ROUNDS = raw_input("> ")
if ROUNDS.isdigit() is False:
    exit_program()
calculate()
