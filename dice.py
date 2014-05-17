import random

def dice(phenny, input):
    try:
        if int(input.group(2))>9000:
            return phenny.say("Fuck off " + str(input.nick) + ", I don't have time to be rolling over 9000 dice")
        if int(input.group(2))<=0:
            return phenny.say("Rolling no dice... 0")
    except:
        pass
    numberOfDice=1
    try:
        numberOfDice=int(input.group(2))
        return phenny.say("Rolling " + str(numberOfDice) + " dice... " + str(dieRolls(numberOfDice)) + "!")
    except:
        return phenny.say("Rolling a dice... " + str(dieRolls(1)) + "!")
dice.commands = ['dice']

def dieRolls(die):
    total=0
    for i in range(0,die):
        total=total+random.randint(1,6)
    return total

def eightball(phenny, input):
    roll=random.randint(1,20)
    if roll==1:
        return phenny.say("It is certain")
    if roll==2:
        return phenny.say("It is decidedly so")
    if roll==3:
        return phenny.say("Without a doubt")
    if roll==4:
        return phenny.say("Yes definitely")
    if roll==5:
        return phenny.say("You may rely on it")
    if roll==6:
        return phenny.say("As I see it, yes")
    if roll==7:
        return phenny.say("Most likely")
    if roll==8:
        return phenny.say("OUtlook good")
    if roll==9:
        return phenny.say("Yes")
    if roll==10:
        return phenny.say("Signs point to yes")
    if roll==11:
        return phenny.say("Reply hazy try again")
    if roll==12:
        return phenny.say("Ask again later")
    if roll==13:
        return phenny.say("Better not tell you now")
    if roll==14:
        return phenny.say("Cannot predict now")
    if roll==15:
        return phenny.say("Concentrate and ask again")
    if roll==16:
        return phenny.say("Don't count on it")
    if roll==17:
        return phenny.say("My reply is no")
    if roll==18:
        return phenny.say("My sources say no")
    if roll==19:
        return phenny.say("Outlook not so good")
    if roll==20:
        return phenny.say("Very doubtful")
eightball.rule = r'$nickname.*[?]'

