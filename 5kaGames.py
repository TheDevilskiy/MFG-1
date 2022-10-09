from audioop import reverse
import random

Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
while True:
    list2=[Rock, Paper, Scissor]
    print(list2[0],list2[1],list2[2])

    Your_choice=int(input("0 for Rock, 1 for Paper, 2 for Scissor" ))

    print(list2[Your_choice])

    Computer_choce = random.randint(0,2)
    print(list2[Computer_choce])

    if Your_choice == 2 and Computer_choce == 0 :
        print ("Your Win")
    elif Computer_choce == 2 and Your_choice == 0:
        print ("Computer Win")

    if Your_choice>Computer_choce:
        print ("Your Win")
    elif Computer_choce>Your_choice:
        print ("Computer Win")

    elif Computer_choce==Your_choice:
        print ("No Win")
