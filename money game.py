
name = input("Enter your name".upper().capitalize())
print(name.lower().capitalize(), "welcome to the game...")
questions = ["what is the capital of the US ?", "what is the capital of Ghana ?", "what is the capital of UK? "]
questions2 = ["what is the capital of Germany? ", "what is the capital of Israel? ", "what is the capital of Nigeria?"]



def moneygame():
       ans_counter = 0
       prem_q = input("who is the president of the US? ").upper().capitalize()
       ans1= "joe biden".upper().capitalize()

       if prem_q == ans1.upper().capitalize():

              print("Let's play ")
       else:
              print("you got it wrong. Let's try a different question")
              quit()

       ans2=input(questions[0]).upper().capitalize()
       ans3=input(questions[1]).upper().capitalize()
       ans4=input(questions[2]).upper().capitalize()



       if ans2 == "washington".upper().capitalize() and ans3 == "accra".upper().capitalize() and ans4 =="london" .upper().capitalize():

              ans_counter +=15

              print("Congratulations, your answers are right and you've entered the money zone ")
       else:
              print("you got the answers wrong, sorry you've lost. ")
              quit()

       ans5 = input(questions2[0]).upper().capitalize()
       ans6 = input(questions2[1]).upper().capitalize()
       ans7 = input(questions2[2]).upper().capitalize()

       if ans5 == "berlin".upper().capitalize() and ans6 == "jerusalem".upper().capitalize() and ans7 == "abuja".upper().capitalize():

              ans_counter +=15

              print("Congratulations, your answers are right")

       else:

              print("sorry, you've lost out")

       print("you have", ans_counter, "total points")



moneygame()




