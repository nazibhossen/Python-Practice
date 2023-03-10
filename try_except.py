# # try:
# #     num1 = 7
# #     num2 = 0
# #     print (num1 / num2)
# #     print("Done calculation")
# # except ZeroDivisionError:
# #     print("An error occurred")
# #     print("due to zero division")

# try:
#   variable = 10
#   print (10 / 2)
# except ZeroDivisionError:
#   print("Error")
# print("Finished")

try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")

