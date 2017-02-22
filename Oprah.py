print "\n"*80
print "Welcome to the Oprah show!"
timBees = 25
bobbyBees = 15
richardBees = 0
bobbyVal = 5
everyoneElse = 100
print "Tim is a bee keeper. He has ", timBees, " bees."
print "Bobby has many of Tim's old bees, they liked him better. He has ", bobbyBees, " bees."
bobbyBees = bobbyBees - bobbyVal
richardBees = richardBees + bobbyVal
print "Some of bobby's bees have escaped and think Richard's wife smells sweet.\n Richard now has ", richardBees, " bees."
print "Bobby currently has ", bobbyBees, " bees."
generosity = int(raw_input("\"How generous are you feeling today Oprah?\"\n"))
print "\n"*80
print "You have given everyone ", generosity, " bees!"
print "Tims bees have had offspring!"
timBees = ((timBees+generosity)/2)**((timBees+generosity)/2)
bobbyBees = bobbyBees + generosity
richardBees = richardBees - richardBees
print "Tim now has ", timBees, " bees."
print "Bobby now has ", bobbyBees, " bees."
print "Richard managed to get stung by all his bees, they  all died."
raw_input("Do you have a bee problem?")
beesTotal = bobbyBees + richardBees + (everyoneElse*generosity)
print "BEES!"*beesTotal
print "I think you have a bee problem."
raw_input()
