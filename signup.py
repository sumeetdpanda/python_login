# Saving User Inputs in a dictionary
def saveInfo(name, email):
  checker = False
  while checker == False:
    password = input("Enter your password: ")
    re_password = input("Enter your password again: ")
    if password == re_password:
      info_dict = {
        "name": name,
        "email": email,
        "password": password
      }
      try:
        save_info = open('database.txt', 'wt')
        save_info.write(str(info_dict))
        save_info.close()
        checker = True
        return "Signup Success"
      except:
        print("Unable to write to database")
    else:
      print("Your passwords are not matching please try again")

# User Inputs
def main_signup():
  print("*Signup Form*")
  name = input("Enter your name: ")
  email = input("Enter your email: ")
  print(saveInfo(name, email))