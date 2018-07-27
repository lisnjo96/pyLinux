current_users=[]
new_users=[]

listed=True

while listed:
  remain=5-len(current_users)
  users=input("type "+str(remain)+" more names please :" )
  current_users.append(users)
  if len(current_users)==5:
    listed=False

print(current_users)
listed=True

while listed:
  remain=5-len(new_users)
  users=input("type "+str(remain)+" more names please :" )
  if users.lower() in map(str.lower,current_users):
    print(users+" has been already in use!")
    print("please try it again.\n")
  elif users.lower() in map(str.lower,new_users):
    print(users+" has been already in use!\nplease try it again.\n")
  elif len(new_users)==2:
    for i in range(2,4):
      new_users.append(current_users[i])
    print(str(len(new_users)-2)+" names been inserted!")
  elif len(new_users)==5:
    listed=False
  else:
    new_users.append(users)
    print(str(len(new_users)))

print(new_users)
print("\n")

remove_list=[]

for new_user in new_users:
  if new_user in current_users:
    print(new_user+" has been already in use!")
    remove_list.append(new_user)
  else:
    print(new_user+" can be used.")

for i in range(0,len(remove_list)):
  new_users.remove(remove_list[i])

print(new_users)
print("\n")

while len(new_users) < 5:
  print("Please insert "+str(5-len(new_users))+"more names!")
  users=input(" :" )
  isAvails=[]
  isAvails.append(users)
  for isAvail in isAvails:
    if isAvail.lower() in map(str.lower,current_users):
      print(isAvail+" has been already in use!")
    elif isAvail.lower() in map(str.lower,new_users):
      print(isAvail+" has been already in use!")
    else:
      new_users.append(isAvail)
      print(new_users)

nameList=current_users+new_users

print("\n")
print("name list: "+str(map(str.title,nameList)))
print("task Ended!")
