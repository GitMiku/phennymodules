import random
#outputs a colorful message

def Kawaiitest(phenny, input):
        x=0
        while x < 5:
                Damn = ""+str(notVeryRandomColor())+",1"+"D"+str(notVeryRandomColor())+",1"+"a"+str(notVeryRandomColor())+",1"+"m"+str(notVeryRandomColor())+",1"+"n"+str(notVeryRandomColor())+",1"
                Nigga = ""+str(notVeryRandomColor())+",1"+"N"+str(notVeryRandomColor())+",1"+"i"+str(notVeryRandomColor())+",1"+"g"+str(notVeryRandomColor())+",1"+"g"+str(notVeryRandomColor())+",1"+"a"+str(notVeryRandomColor())+",1"
                Thats = ""+str(notVeryRandomColor())+",1"+"T"+str(notVeryRandomColor())+",1"+"h"+str(notVeryRandomColor())+",1"+"a"+str(notVeryRandomColor())+",1"+"t"+str(notVeryRandomColor())+",1"+"'"+str(notVeryRandomColor())+",1"+"s"
                Kawaii = ""+str(notVeryRandomColor())+",1"+"K"+str(notVeryRandomColor())+",1"+"a"+str(notVeryRandomColor())+",1"+"w"+str(notVeryRandomColor())+",1"+"a"+str(notVeryRandomColor())+",1"+"i"+str(notVeryRandomColor())+",1"+"i"+str(notVeryRandomColor())+",1"+"!"+str(notVeryRandomColor())+",1"+"!"
                x+=1
phenny.say(Damn + " " + Nigga + " " + Thats + " " + Kawaii)
Kawaiitest.commands = ['Kawaii', 'Cute', 'cute', 'kawaii', 'omg', 'OMG']

def notVeryRandomColor():
x=(random.sample([13,12,11,9,8,6,4], 1))	
        try:
                return int(str(x)[1:3])
        except ValueError:
                pass
        try:
                return int(str(x)[1:2])
        except ValueError:
                pass

