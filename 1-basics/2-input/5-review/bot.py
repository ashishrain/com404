#Creating a ascii face through an app

#storing characters for eyes, nose and mouth into their respective variables
print("Please enter a character for eyes")
eye = str(input())

print("Please enter a character for nose")
nose = str(input())

print("Please enter a character for mouth")
mouth = str(input())

print("Please enter a character for ears")
ears = str(input())

#displays the face
print("""
The ascii face that you created is:

  ----------
  |        |
  |  """ + eye + "  " + eye + """  |
 """ + ears + """|        |""" + ears + """
  |   """ + nose + nose + """   |
  |        |
  |  """ + mouth + mouth + mouth + mouth + """  |
  |        |
  ----------""")