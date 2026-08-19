#Add entry
#View Entry
#Search entry
#delete entry
#exit
from datetime import datetime
def add_e():
  v = input("What would you like to enter in the journal?")
  f = open("file.txt","a")
  t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  f.write("\n[{}] {}".format(t,v))
  print("Entry has been saved")
# View the file
def view_e():
  f = open("file.txt","r")
  for i in f:
    print(i)
  f.close()
# Searching an entry
def search_e():
  p = input("Enter a keyword to search")
  found = False
  f = open("file.txt","r")
  print("Your search results are:")
  for i in f:
    if p in i:
      print(i)
      found = True
  if found == False:
    print("The keyword you searched is not available")
# deleting a file
def delete_e():
  file=open("file.txt","r")
  lines = file.readlines()
  b = int(input("What line do you want to delete"))
  if b >= 0 and b < len(lines):
    del lines[b]
    print("The line has been deleted")
    file=open("file.txt","w")
    for i in lines:
      file.write(i)
    file.close()
  
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
  elif x == 2:
    view_e()
  elif x == 3:
    search_e()
  elif x == 4:
    delete_e()
  elif x == 5:
    break
