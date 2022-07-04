#6.1 and 6.4
person_i_know = {
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'age': 'age',
    'city': 'city',
}

for key, value in person_i_know.items():
    print(f"{key} = {value}")

print("")

#6.2 and 6.4
favorite_numbers = {
    'person1': 1,
    'person2': 2,
    'person3': 3,
    'person4': 4,
    'person5': 5,
}

for key, value in favorite_numbers.items():
    print(f"{key} = {value}")

print("")

#6.5
rivers = {
    'nile': 'egypt',
    'river2': 'country2',
    'river3': 'country3',
}

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)

print("")

#6.5
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
should_take_favorite = ['friend1','friend2','sarah','phil','friend3']

for name in should_take_favorite:
    print(name.title())
    if name not in favorite_languages.keys():
        print(f"\t{name.title()}, please take our poll!")
    else:
        print(f"\t{name.title()}, thx")