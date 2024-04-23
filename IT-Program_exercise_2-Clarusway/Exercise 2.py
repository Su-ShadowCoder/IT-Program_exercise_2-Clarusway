# # Exercise 1:
# name = "sudarshen kandasamy"
# age = "29 years old"
# hobby = ("loves coding, going to the gym and reading novels with a cup of "
#          "coffee.")
# place = "Amsterdam."
# course = "Clarusway course"
# print(f"Hi, my name is {name} and i am {age}. \n"
#       f"I {hobby}\n"
#       f"I was born and grew up in the city of {place} \n"
#       f"and now i am following the {course}.")
#
# # Exercise 2:
# first_sentence = "I am fabulous,"
# second_sentence = "I try to stay humble,"
# third_sentence = "but I'm mostly grateful."
# space = " "
#
# print(f"{first_sentence} {second_sentence} {third_sentence}")
# print(first_sentence, second_sentence, third_sentence)
# print(first_sentence + space + second_sentence + space + third_sentence)
#
# #Exercise 3:
#
# user_input = input("Write something down, \n"
#                    "and i will tell you if what you wrote is longer or "
#                    "shorter than 10 characters! \n"
#                    "Enter your sentence: ")
# if (len(user_input)) > 10:
#     print("This string has more than 10 characters! ")
# else:
#     print("This string has 10 or shorter than 10  characters!")
#
# # Exercise 4:
# user_input = input("Enter something!: ")
# char_numb = (len(user_input))
# if (len(user_input)) % 3 == 0:
#     print(f"This string is {char_numb} characters long!")
#     print(user_input[::-1])
# else:
#     print(f"This string is {char_numb} characters long!")
#     print(user_input)
#
# # Exercise 5:
# user_input = input("Enter something!: ")
# print(user_input[:3] + user_input[-3:])
#
# # Exercise 6:
# user_input = input("Enter a 'number' or a 'word', "
#                    "and I will check if your\n"
#                    "entered value is a palindrome or not!: ")
# reverse = user_input[::-1]
# if user_input == reverse:
#     print("This IS a palindrome!")
# else:
#     print("This is NOT a palindrome!")
