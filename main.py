import json
import random
import string
from pathlib import Path

class Bank:
     database = 'data.json'
     data = []

     try:
        if Path(database).exists():
            with open (database) as fs:
                    data = json.loads(fs.read())
        else:
            print(" NO SUCH FILE EXSITS ")            
     except Exception as err:
      print(f" THE ERROR OCCURED  AS {err}")

     @classmethod
     def __update(cls):
          with open(cls.database,'w') as fs:
              fs.write(json.dumps(Bank.data))

     @classmethod
     def __accoountgenerate(cls):
         alpha = random.choices(string.ascii_letters,k=4)
         num = random.choices(string.digits,k=4)
         spchar = random.choices('!@#$%^&*',k=2)
         id = alpha+num+spchar 
         random.shuffle(id) # ham yaha shuffle ka use line sa join na ho alag alag pattern ma har baar uske liya kar rhe hai 
         return "".join(id)         
     
    

     def Createaccount( self ):
          info = {
              "NAME" : input(" TELL ME YOUR NAME :- "),
              "AGE" : int(input(" TELL ME YOUR AGE :- ")),
              "EMAIL" : input(" TELL ME YOUR EMAIL :- "),
              "PIN": int(input(" TELL ME YOUR 4 DIGIT PIN :- ")),
              "ACCOUNT_NO." : Bank.__accoountgenerate(),
              "BANK_BALANCE" : 0  
          }
          if info[' AGE '] < 18 or len(str(info[' PIN '])) != 4 :
              print(" YOU CANNOT CREATE THE BAK ACOUNT ")

          else:
              print(" YOUR ACCOUNT HAS BEEN CREATED SUCCESFULLY ") 
              for i in info :
                  print(f" {i} : {info[i]} ")
              print(" PLEASE NOTE DOWN YOUR ACCOUNT NO. CAREFULLY ")

              Bank.data.append(info)
              Bank.__update()        

     def depositmoney(self):
         accnumber = input(" PLEASE ENTER YOUR BANK ACCOUNT NO. ")
         pin = int(input(" PLEASE ENTER YOUR PIN AS WELL"))

         userdata = [i for i in Bank.data if i[' ACCOUNT_NO.'] == accnumber and i[' PIN '] == pin]

         if userdata == False :
             print("SORRY NO DATA FOUND")
         else:
             amount = int(input(" HOW MUCH MONEEY DO YOU WANT TO DEPOSIT "))
             if amount > 10000 or amount < 0:
                 print(" THE AMOUNT IS TOO MUCH YOU CAN DEPOSITE BELOW 10000 AND ABOVE 0 ")
             else:
                 userdata[0]['BANK_BALANCE'] += amount
                 Bank.__update()
                 print(" YOUR AMOUNT DEPOSITED SUCESSFULLY")

     def withdrawmoney(self):
         accnumber = input(" PLEASE ENTER YOUR BANK ACCOUNT NO.")
         pin = int(input(" PLEASE ENTER YOUR PIN AS WELL "))

         userdata = [i for i in Bank.data if i[' ACCOUNT_NO.'] == accnumber and i[' PIN '] == pin]

         if userdata == False :
             print(" SORRY NO DATA FOUND")
         else:
             amount = int(input(" HOW MUCH MONEEY DO YOU WANT TO WITHDRAW "))
             if userdata[0]['BANK_BALANCE'] < amount:
                 print(" INSUFFICENT BALANCE ")
             else:
                 userdata[0]['BANK_BALANCE'] -= amount
                 Bank.__update() 
                 print(" YOUR AMOUNT WITHDREW SUCESSFULLY")


     def showdetails(self):       
         accnumber = input(" PLEASE ENTER YOUR BANK ACCOUNT NO.")
         pin = int(input(" PLEASE ENTER YOUR PIN AS WELL "))

         userdata = [i for i in Bank.data if i[' ACCOUNT_NO.'] == accnumber and i[' PIN '] == pin]
         print(" YOUR INORMATION ARE : \n\n\n")
         for i in userdata[0]:
             print(f" {i} : {userdata[0][i]} ")

     def updatedetails(self):
         accnumber = input(" PLEASE ENTER YOUR BANK ACCOUNT NO.")
         pin = int(input(" PLEASE ENTER YOUR PIN AS WELL "))

         userdata = [i for i in Bank.data if i[' ACCOUNT_NO.'] == accnumber and i[' PIN '] == pin]

         if userdata == False:
             print(" THIS USER IS NOT FOUND :")
         else:
             print(" YOU CANNOT CHANGE THE ACCOUNT NO., BALANCE AND AGE :")
             print(" FILL THE DETAILS FOR THE CHANGES AND LEAVE IT EMPTY FOR NO CHNAGE :")

             newdata = {
                 " NAME " : input(" PLEASE ENTER YOUR NEW NAME OR PRESS ENTER FOR NO CHANGEMENT : "),
                 " EMAIL " : input(" PLEASE ENTER YOUR NEW EMAIL OR PRESS ENTER FOR NO CHANGEMENT : "),
                 " PIN " : input(" PLEASE ENTER YOUR NEW PIN  OR PRESS ENTER FOR NO CHANGEMENT : ")
                }
             if newdata[" NAME "] == "" :
                 newdata[" NAME "] = userdata[0][' NAME '] 
             if newdata[" EMAIL "] == "" :
                 newdata[" EMAIL "] = userdata[0][' EMAIL ']      
             if newdata[" PIN "] == "" :
                 newdata[" PIN "] = userdata[0][' PIN ']

             newdata [' AGE '] = userdata[0][' AGE ']
             newdata [' ACCOUNT_NO.'] = userdata[0][' ACCOUNT_NO.']
             newdata ['BANK_BALANCE'] = userdata[0]['BANK_BALANCE']

             if type(newdata) == str :
                 newdata[' PIN '] = int(newdata[' PIN '])

             for i in newdata :
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

             Bank.__update()
             print(" YOUR DETAILS ARE UPDATED SUCESSFULLY : ")                     
                                 
     def delete(self):
         accnumber = input(" PLEASE ENTER YOUR BANK ACCOUNT NO.")
         pin = int(input(" PLEASE ENTER YOUR PIN AS WELL "))

         userdata = [i for i in Bank.data if i[' ACCOUNT_NO.'] == accnumber and i[' PIN '] == pin]

         if userdata == False:
             print(" USER NOT FOUND : ")
         else:
             check= input(" PRESS Y FOR DELTEING IF YIU ACTUALLY WANT TO DELETE THE DATA OR PRESS N : ")
             if check == 'n' or check == 'N':
                 print(" by pass ")
             else:
                 index = Bank.data.index(userdata[0])
                 Bank.data.pop(index)
                 Bank.__update()

                 print(" THE DATA IS DELETED SUCESSFULLY")

user = Bank()

print(" PRESS 1 FOR CREATING A BANK ACCOUNT ")
print(" PRESS 2 FOR DEPOSTING THE MONEY IN BANK ACCOUNT ")
print(" PRESS 3 FOR WITHDRAWING MONEY IN YOUR BANK ACCOUNT ")
print(" PRESS 4 FOR DETAILS ")
print(" PRESS 5 FOR UPDATING THE DETAILS ")
print(" PRESS 6 FOR DELETING THE ACCOUNT ")

check = int(input(" TELL ME YOUR RESPONSE :- "))

if check == 1:
     user.Createaccount()
elif check == 2 :
    user.depositmoney()
elif check == 3:
    user.withdrawmoney()
elif check == 4:
    user.showdetails()     
elif check == 5:
    user.updatedetails() 
elif check == 6 :
    user.delete()           



