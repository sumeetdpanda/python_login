from login import main_login
from signup import main_signup


def get_selection(selection):
  checker = False
  while checker == False:
    if selection.lower() == 'login' or selection.lower() == 'l':
      main_login()
      checker = True
    elif selection.lower() == 'signup' or selection.lower() == 's':
      main_signup()
      selection_2 = input("Do you want to sign in now? (Y/N): ")
      if selection_2.lower() == 'y':
        main_login()
      elif selection_2.lower() == 'n':
        break
      checker = True
    else:
      print('Wrong Selection, Please try again!!')
      main_selection()

def main_selection():
  selection = input("What do you want to do Login/Signup ? : ")
  get_selection(selection)

main_selection()