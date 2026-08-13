#Add entry
#View Entry
#Search entry
#delete entry
#exit
from datetime import datetime
def add_e():
  v = input("What would you like to enter in the journal?")
  f = open("file.txt","a")
  f.write("\n {}".format(v))
  print("Entry has been saved")
while True:
  print("---Menu---")
  print("1. Add entry")
  print("2. View Entry")
  print("3. Search entry")
  print("4. delete entry")
  print("5. exit")
  x = int(input("Choose an option(1-5)"))
  if x == 1:
    add_e()
  elif x == 5:
    break
