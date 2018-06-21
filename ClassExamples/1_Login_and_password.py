username = 'Aleksey'
user_password = 'xt2*uA'
matched = False
while(True):
   login_name = input('Pls enter yout name:')
   if username == login_name:
      for i in range(3):
         password = input('enter your password:')
         if user_password == password:
            print("Hello " + login + "!")
            matched = True
            break
      if matched:
         break
      else:
         print('Sorry too many tries')
   else:
      print('Wrong username.Pls Try again')
