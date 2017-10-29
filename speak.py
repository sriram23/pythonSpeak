import os

Name = raw_input("Please Enter your name:")
os.system("espeak Hello"+Name+" -s 120")
print "Please Enter the sentence to speak:"
os.system("espeak 'Please Enter the sentence to speak' -s 120")
sentence = raw_input()
print "You have entered: "+sentence
os.system("espeak 'You have entered"+sentence+"' -s 120")

