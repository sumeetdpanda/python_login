import ast
import mysql.connector

mydb = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'sumeet@1996',
  database = 'python_login'
)

mycursor = mydb.cursor()

def login(email,passw):
  sqlFormulaSELECT = 'SELECT * FROM user WHERE email = %s'
  mycursor.execute(sqlFormulaSELECT,(email,))
  myresult = mycursor.fetchall()
  for result in myresult:
    if passw == result[2]:
      print("Login Success")
      print("Name is {} with email {} and password {}".format(result[0], result[1], result[2]))
    else:
      print("*Wrong Credentials, please try again!!!*")
      main_login()

def main_login():
  email = input("Enter Email: ")
  passw = input("Enter Password: ")
  login(email, passw)