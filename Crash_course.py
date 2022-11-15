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

####--IF AND ELSE AND ELIF--####

# age = int(input('Please enter your age: \n'))
# if age < 4:
#     price = 20
#     # print("Adission fee is Rs 20")
# elif age < 18:
#     price = 25
#     # print("admission fee is Rs 25")
# elif age >=60:
#     price = 50
#     # print("admission fee is Rs 50")
# print(f'Your admission cost is {price}')

# alien_color = 'green'
#
# if alien_color == "blue":
#     print("Player just earned 5 points")
# else:
#     print("Player just earned 10 points")

# # alien_color = 'green'
# alien_color = 'yellow'
# alien_color = 'red'
#
# if alien_color == "green":
#     print("Player just earned 5 points")
# elif alien_color == 'yellow':
#     print("player just earned 10 points")
# else:
#     print("Player just earned 20 points")


# age = int(input('Please enter your age: \n'))
# if age < 2:
#     print("You are a baby.!")
# elif age >= 2 and age < 4:
#     print("You are a toddler.!")
# elif age >= 4 and age < 13:
#     print("you are a kid.!")
# elif age >= 13 and age < 20:
#     print("you are a teenager.!")
# elif age >= 20 and age < 65:
#     print("you are an adult.!")
# else:
#     print("you are an elder.!")

# fav_fruit = ['apple','mango','grapes','orange','pineapple']
# if 'apple' in fav_fruit:
#     print('You really like apple')
# if 'mango' in fav_fruit:
#     print("\nyou really like mango")
# if 'grapes' in fav_fruit:
#     print("\nyou really like grapes")
# if 'orange' in fav_fruit:
#     print("\nyou really like orange")
# if 'pineapple' in fav_fruit:
#     print("\nyou really like pineapple")


# available_toppings = ['mushroom','olives','green peppers','pepparoni','pineapple','extra cheese']
# requested_toppings = ['olives','green peppers','mushroom','french fries']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f'adding {requested_topping.title()}')
#     else:
#         print(f"sorry we dont have {requested_topping.title()}")
# print('\nfinished making your pizza')

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f'Adding {requested_topping} ')
#         print('Finished making your pizza')
# print("\nDo you really need a plain pizza")

# names = ['admin','abhi_h','anu_h','sonu_k']
# names = []
# if names:
#     for name in names:
#         if name == 'admin':
#             print("Hello Admin, would you like to see a status report?")
#         else:
#             print(f"Hello {name.title()}, thank you for logging in again.!")
# else:
#     # print(f"Hello {name}, thank you for logging in again.!")
#     print("We need to find some users.!")
# print('\nThank you have a Great day..!')

# current_users = ['abhi_h','anu_h','SONU_K']
# new_users = ['sonu_k','moni_k','abhi_h','anu_h']
#
# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print('You need to create a new username'.title())
#     else:
#         print('username is available'.title())

# num = [1,2,3,4,5,6,7,8,9]
# for i in num:
#     # print(i)
#     if i == 1 :
#         print(i,'st')
#     elif i == 2:
#         print(i,'nd')
#     elif i == 3:
#         print(i,'rd')
#     else:
#         print(i,'th')

###----DICTIONARY----####

# alien_0 = {'color':'green', 'points':5}
# # print(alien_0['points'])
# # print(alien_0['color'])
# print(alien_0)
# alien_0={}
# alien_0['x_coordinate']= 0
# alien_0['y_coordinate'] = 30
# alien_0['speed']='medium'
# # print(f"The color of alien is {alien_0['color']}".title())
# print(f"original-position: {alien_0['x_coordinate']}".title())
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_coordinate']= alien_0['x_coordinate']+ x_increment
# print(f"new x_position: {alien_0['x_coordinate']}".title())

# name = "s3://amazon.com"
# def get_name(name:str):
#     not_name = False
#     not_namee = False
#     name1 = 's3://aws.com'.lower()
#     if name[:len(name1)].lower()!= name1:
#         not_name = True
#     name2 = 'hariii'.lower()
#     if name[:len(name2)].lower()!= name2:
#         not_namee = True
#     if not_name and not_namee:
#         name = 'H'+ name
#     # if (not_namee == False):
#     #     name = "a"+ name
#         return name
# print(get_name("satya"))

# DICTIONARY GET

# name = {'abhi':'hari','anu':'hari'}
# # print(name['satya'])
# print_value = name.get('satya','No key_value for the key = satya')
# print(print_value)
# details = {
#     'name':'abhi',
#     'lname':'hari',
#     'age':30,
#     'address':'Hyderabad'
# }
# print(details)
# print(details['name'])
# print(details['lname'])
# print(details['age'])
# print(details['address'])

# for i in details:
#     print(i,':',details[i])
# for i,j in details.items():
#     print(i,':',j)

# user = {
#     'username': 'abhi',
#     'first':"a",
#     'last':'H'
# }
# for key,value in user.items():
#     print(f'\nkey:{key}')
#     print(f'value:{value}')

# fav_languages = {
#     'abhi':'python',
#     'anu':'java',
#     'satya':'javascript'
# }
# for name,language in fav_languages.items():
#     print(f"{name.title()}'s fav language is {language}.")
# friends = ['abhi','anu']
# for name in fav_languages.keys():
#     print(f'Hi {name.title()}')
#
#     if name in friends:
#         language = fav_languages[name].title()
#         print(f'\t{name.title()},I see you love {language}')
# if 'moni' not in fav_languages.keys():
#     print('Moni please take a poll')

# for name in sorted(fav_languages.keys()):
#     print(f'{name.title()}. Thank you for taking the poll')

# details = {
#     'name':'abhi',
#     'lname':'hari',
#     'age':30,
#     'address':'Hyderabad'
# }
#
# for key,value in details.items():
#     print(f'{key}:{value}')

# dict = {
#     'delhi':'hyd',
#     'hyd':'telangana',
#     'raksha':'hyd'
# }

# for key,value in dict.items():
#     print(f'{key.title()} is the capital of {value.title()}')
# for key in dict.keys():
#     print(f'{key.title()}')
#
# for value in dict.values():
#     print(f'{value.title()}')

# fav_languages = {
#     'abhi':'python',
#     'anu':'java',
#     'satya':'javascript'
# }
# friends = ['satya','moni','abhi','anu','sonu']
#
# for i in friends:
#     if i in fav_languages.keys():
#         print(f'{i.title()}. Thanks for taking the poll')
#     else:
#         print(f'{i.title()} Sorry, You need to take the poll')

####----NESTED-DICT----####

# friends = {'color':'Green','speed':'Slow','points':5}
# friends2 = {'color':'Yellow','speed':'Slow','points':15}
# friends3 = [friends,friends2]
# print(friends3)

# dict = []
#
# for dict_num in range(5):
#     new_dict = {'name':'abhi','age':30}
#     dict.append(new_dict)
#     # print(dict)
# for i in dict[:3]:
#     print(dict)
# print('.....')
# #
# # print(f'\nTotal number of aliens added {len(dict)}')
#
# for i in dict[:2]:
#     if i['name'] == 'abhi':
#         i['name'] = 'Abhinay'
#         i['age'] = 29
#         print(dict)

# pizza = {
#     'crust':'thick',
#     'toppings':['mushrooms','pepparoni']
# }
# print(f"You have ordered a {pizza['crust']}-crust pizza With the toppings:")
# # print('')
# for topping in pizza['toppings']:
#     print('\t'+ topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }
# for name,languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favourite languages are: ")
#     for language in languages:
#         print(f'\t{language.title()}')

# favorite_languages = {
#     'Abhi': ['python'],
#     'Anu': ['c','Java'],
#     'edward': ['ruby'],
#     'phil': ['python', 'haskell'],
# }
#
# for name,languages in favorite_languages.items():
#     if len(languages)<=1:
#         print(f"{name.title()}'s fav language is: ")
#     else:
#         print(f"{name.title()}'s fav languages are: ")
#     for language in languages:
#         print(f"\t{language.title()}")

# users = {
#     'abhi':{
#         'fname':'Hari',
#         'lname':'Abhi',
#         'age':30
#     },
#     'anu':{
#         'fname':'Hari',
#         'lname':'Anu',
#         'age':28
#     },
#     'satya':{
#         'fname':'Hari',
#         'lname':'Satya',
#         'age':27
#     }
# }
# # for username,user_info in users.items():
# #     print(f"\nusername:{username}")
# #     full_name = f"{user_info['fname']} {user_info['lname']}"
# #     age = f"{user_info['age']}"
# #
# #     print(f"\tfull_name = {full_name.title()}")
# #     print(f"\tAge= {age.title()}")
#
# for name,info in users.items():
#     print(f"username = {name}")
#     full_name = f"{info['fname']}-{info['lname']}"
#     age = f"{info['age']}"
#
#     print(f"\tFullname = {full_name}")
#     print(f"\tAge = {age}")

# user1 = {
#     'name':'abhi',
#     'age':30
# }
# user2 = {
#     'name':'anu',
#     'age':28
# }
#
# people = [user1,user2]
# print(people)
# for i in people:
#     print(f"{i['name']} {i['age']}")

# pet = {
#     'name':'DOG',
#     'nature':'faithful',
#     'owner': 'abhi'
# }
# owner = {
#     'name':'cat',
#     'nature':'cunning',
#     'owner':'anu'
# }
# pets = [pet,owner]
# # print(pets)
#
# for i in pets:
#     print(f"A {i['name'].title()} is a {i['nature']} and its owner is {i['owner'].title()}")

####----INPUT AND WHILE_LOOP----####

# rental_car = input("What kind of rental car you would like?\n")
# print(f"let me find you a {rental_car}")
# question = input("How many people are in your dinner group?\n ")
# question = int(question)
# if question >8:
#     print("I am sorry you need to wait for the table to get ready..!")
# else:
#     print("Your table is ready.!")

# ten = int(input("Enter a number: \n"))
# if ten % 10 ==0:
#     print(f"{ten} is the multiple of 10.!")
# else:
#     print(f"{ten} is not the multiple of 10.!")
