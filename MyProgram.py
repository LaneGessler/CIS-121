"""
#Name Lane Gessler
#Date 10/24/2022

#What does this do? creates RoboFriends
"""

from ClassFile import RoboFriend

bob = RoboFriend("Bob",20)
charley = RoboFriend("Charley",23)
notaRobot = RoboFriend("notaRobot",2)

bob.stateName()
bob.stateAge()
charley.stateName()
charley.stateAge()
notaRobot.stateName()
notaRobot.stateAge()
