# v = "morning"
v = "good morning"
# v3 = v
# print(v3)
# print(v.title())
# print(f"Hello, {v.title()} ")
#
# first_name = "hari"
# last_name = "abhinay"
#
# print(f"Hello,{first_name.title()} {last_name.title()}")
# message = "Hello,{} {}".format(first_name,last_name)
# print(message.title())
#
# name = "albert einstein"
#
# message = ' " a person who never made a mistake never made anything new" '
#
# result = "{} once said,{}".format(name.title(),message.title())
# print(result)
#
# Name = "hari abhinay"
# print(Name.title(),Name.upper(),Name.lower())
#
# name1 = "Eric"
# message = '"Hello {},would you like to learn some python today?"'.format(name1)
# print(message)


# with open("hello.txt","w") as my_file:
#     my_file.write("welcome to the new file\n")
#     my_file.write("this is just a trial\n")
#     my_file.write("Goodbye!")

# bikes = ['pulsar','honda','scooter','activa','cbz','apache']
# # message = f'my first bike is {bikes[0].title().}'
# message = 'my first bike is {}'.format(bikes[0].title())
# print(message)

# names = ['abhi','anu','sonu','moni']
#
#
# pop_out = names.pop(0)
# pop_out1 = names.pop(1)

# names.insert(0,'satya')
# names.insert(2,'anurag')
# names.append('yashu')
# print(names)
# names2 = names
# del names2[0]
# del names2[0]
# print(names2)
# print(f'sorry {pop_out.title()}. I cannot invite you to the dinner')
# print(f'sorry {pop_out1.title()}. I cannot invite you to the dinner')
# for i in names:
# modified_mem = names[3]
# names[3] = 'Azu'
# print("hi {}, i would like to invite you to dinner. Thank you!".format(names[0].title()))
# print("hi {}, i would like to invite you to dinner. Thank you!".format(names[1].title()))
# print("hi {}, i would like to invite you to dinner. Thank you!".format(names[2].title()))
# print("hi {}, i would like to invite you to dinner. Thank you!".format(names[3].title()))
# print(f'{modified_mem} couldn't attend the dinner')
# print(modified_mem)
# for i in names:
#     print('\nhi {}, you are till invited to dinner'.format(i))
#     print('hi {} i have found a bigger dinner table'.format(i))
#     print(i)
#     print("my name is {}".format(i))
# m = 'you can only invite two people..!'
# print(m.upper())
# brands = ['bajaj','honda','hero']
# m1 = f'my fav brand is {brands[2].title()}'
# m2 = f'but i drive {brands[0].title()}'
# m3 = f'present i have {brands[1].title()}'
# brands.insert(0,'hero honda')
# print(brands)

# print(m1)
# print(m2)
# print(m3)

# info = ['abhi','anu']
# # 1.append the list; 2.del item from the list; 3.pop from the list; 4.insert into the list
#
# info.append('yashu')
# print(info)
# del info[1]
# print(info)
# info.pop(0)
# print(info)
# info.insert(1,'abhi')
# print(info)

# cars = ['audi','bmw','duster','ferrari']
# print(len(cars))
# print('Here is the original list:')
# print(cars)
# print('\n Here is the sorted list:')
# print(sorted(cars))
# print(cars)
# cars.reverse()
# print(cars)

# places = ['lxpt','mncl','gdk','hyd','rme']
# print(places)
# print(sorted(places))
# print('\n Here is the original list:')
# print(places)
# places.reverse()
# print(places)
# places.reverse()
# print(places)
# places.sort()
# print(places)
# foods = ['rice','curry','egg','apple','curd']
# print(foods)
# z = foods[0:3]
# x = foods[1:4]
# y = foods[-3:]
# print('\n The first three items in the list are: ')
# print(z)
# print('\nThe middle items in the list are: ')
# print(x)
# print('\nThe last three items in the list are: ')
# print(y)
# my_foods = foods[:]
# my_foods.append('ice cream')
# print(my_foods)
# for food in foods:
#     print(food)
# for my_food in my_foods:
#     print(my_food)


####-- TUPLES --####

# dimensions = (20,30)
# print('\noriginal dimensions: ')
# for dimension in dimensions:
#     print(dimension)
#
# dimensions = (40,50)
# print('\nmodified domentions are: ')
# for dimension in dimensions:
#     print(dimension)

# foods = ('pasta','macaroni','zuccini','lasagna')
# foods[1] = 'cheese'
# print(foods)
# print("\nRestaurant's original menu: ")
# for food in foods:
#     print(food.title())
#
# foods = ('pasta','lasagna')
# print("\nRestaurant's modified menu: ")
# for food in foods:
#     print(food.title())

cars = ['audi','benz','tata','toyota']
# if 'audi' in cars:
#     print('yes its in the cars list')
#
# else:
#     print('Sorry..!')
# for car in cars:
#     if car == 'zumba':
#         print(car.upper())
#     else:
#         print(car.title())

car = 'audi'

# if car != 'zoom':
#     print('Try again')