favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

print("")

for name in favorite_languages:
    print(name.title())

print("")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("")

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

print(favorite_languages)
print(favorite_languages.keys())
print(favorite_languages.values())
print(favorite_languages.items())

print("")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())