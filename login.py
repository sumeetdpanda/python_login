import ast

def login(email,passw):
  checker = False
  file = open('database.txt', 'r')
  content = ast.literal_eval(file.read())
  while checker == False:
    if email == content['email'] and passw == content['password']:
      print("Login Success")
      print("Name is {name} with email {email} and password {password}".format(**content))
      checker = True
    else:
      print("*Wrong Credentials, please try again!!!*")
      main_login()

def main_login():
  email = input("Enter Email: ")
  passw = input("Enter Password: ")
  login(email, passw)