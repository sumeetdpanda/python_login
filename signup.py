import mysql.connector

# Saving User Inputs in a dictionary
def saveInfo(name, email):

  # Databse Initialization
  mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'sumeet@1996',
    database = 'python_login'
  )

  mycursor = mydb.cursor()
  sqlFormulaInsert = 'INSERT INTO user (name, email, password) VALUES(%s, %s, %s)'

  checker = False
  email_exist = False
  while checker == False:
    password = input("Enter your password: ")
    re_password = input("Enter your password again: ")
    if password == re_password:
      mycursor.execute("SELECT email FROM user WHERE email=%s", (email,))
      result = mycursor.fetchall()
      if len(result) == 0:
        try:
          info_tup = (name, email, password)
          mycursor.execute(sqlFormulaInsert, info_tup)
          mydb.commit()
          checker = True
          print("Signup Success")
        except:
          print("Unable to write to database")
      else:
        email_exist = True
        print("Email already exist!! Please try again")
        break
    else:
      print("Your passwords are not matching please try again")
  
  if email_exist == True:
    main_signup()

# User Inputs
def main_signup():
  print("*Signup Form*")
  name = input("Enter your name: ")
  email = input("Enter your email: ")
  saveInfo(name, email)

