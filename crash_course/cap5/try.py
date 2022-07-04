#5.3
alien_color='red'
if alien_color=='green':
    print('You earned 5 points!')
elif alien_color=='yellow':
    print('You earned 10 points!')
elif alien_color=='red':
    print('You earned 15 points!')

print('')

#5.4
age=34
if age<2:
    print('You are a baby!')
if age>=2 and age<4:
    print('You are a toddler!')
if age>=4 and age<13:
    print('You are a kid!')
if age>=13 and age<20:
    print('You are a teenager...')
if age>=20 and age<65:
    print('You are an adult.')
if age>=65:
    print('You are an elder.')

print('')

#5.5
favorite_fruit=['banana','mexerica','pêssego']
if'mexerica'in favorite_fruit:
    print('You really like mexerica') 

print('')

#5.8 - #5.9
#usernames=['user1','user2','user3','user4','admin']
usernames=[]

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

print("")

#5.10
current_users=['User1','User2','User3','user4','user5']
current_users_lower=[x.lower() for x in current_users]
new_users=['newUser1','user2','newUser3','user4','newUser5']
new_users_lower=[x.lower() for x in new_users]

for new_user_lower in new_users_lower:
    if new_user_lower in current_users_lower:
        print(f"{new_user_lower.title()} has already been used.")
    else:
        print(f"{new_user_lower.title()} is available.")

#5.11
numbers=[1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    if number == 2:
        print(f"{number}nd")
    if number == 3:
        print(f"{number}rd")
    if number > 3:
        print(f"{number}th")