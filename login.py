import ast

def login(email,passw, mycursor):
  sqlFormulaSELECT = 'SELECT * FROM user WHERE email = %s'
  mycursor.execute(sqlFormulaSELECT,(email,))
  myresult = mycursor.fetchall()
  for result in myresult:
    if passw == result[2]:
      print("Login Success")
      print("Name is {} with email {} and password {}".format(result[0], result[1], result[2]))
    else:
      print("*Wrong Credentials, please try again!!!*")
      main_login(mycursor)

def main_login(cursor):
  email = input("Enter Email: ")
  passw = input("Enter Password: ")
  login(email, passw, cursor)