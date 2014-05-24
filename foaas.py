import urllib2

def fuckoff(phenny, input):
    arg=input.group(2)
    if "help" in arg[0:4]:
        return phenny.say("http://foaas.herokuapp.com/")
    req=urllib2.Request("http://foaas.herokuapp.com" + arg)
    req.add_header("Accept", "text/plain")
    try:
        response=urllib2.urlopen(req).read()
    except urllib2.URLError:
        return phenny.say("Cannot resolve " + "http://foaas.herokuapp.com" + arg)
    if "<html>" in response:
        return phenny.say("Not a valid argument")
    else:
        return phenny.say(response)
fuckoff.commands = ['fuckoff', 'fu', 'fuck']
