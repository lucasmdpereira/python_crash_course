#4.1
pizzas=['pepperoni','marguerita','lombo']
for pizza in pizzas:
    print(f'I like {pizza} pizza')
print('I really love pizza!')

print('')

#4.2
animals=['dog','cat','pig']
for animal in animals:
    print(f'A {animal} would make a great pet.')
print('Any of these animals would make a great pet')

print('')

#4.3
numbers=[number for number in range(1,21)]
for number in numbers:
    print(number)

print('')

#4.5
million=[number for number in range(1,1_000_001)]
print(min(million))
print(max(million))
millionSum=sum(million)
print(millionSum)

print('')

#4.6
oddNumbers=[oddNumber for oddNumber in range(1,20,2)]
for oddNumber in oddNumbers:
    print(oddNumber)

print('')

#4.7
multiplesBy3=[multipleBy3 for multipleBy3 in range(3,31,3)]
for multipleBy3 in multiplesBy3:
    print(multipleBy3)

print('')

#4.8 and 4.9
cubes=[cube**3 for cube in range(1,11)]
for cube in cubes:
    print(cube)

print('')

#4.10
my_foods=['pizza','falafel','carro cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f'The first two items in the list are:{my_foods[:2]}')
print(f'Two items from the middle of the list are:{my_foods[1:-1]}')
print(f'The last two items in the list are:{my_foods[2:]}')

print('')

#4.11 with #4.1
friend_pizzas=pizzas[:]
pizzas.append('Sabor 1')
friend_pizzas.append('Sabor 2')

print(f'My favorite pizzas are:')
for pizza in pizzas:
    print(f'{pizza}')

print(f'My friend favorite pizzas are:')
for pizza in friend_pizzas:
    print(f'{pizza}')