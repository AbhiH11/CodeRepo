# v = "morning"
# # v = "good morning"
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
#
#
# with open("hello.txt","w") as my_file:
#     my_file.write("welcome to the new file\n")
#     my_file.write("this is just a trial\n")
#     my_file.write("Goodbye!")
#
# bikes = ['pulsar','honda','scooter','activa','cbz','apache']
# # message = f'my first bike is {bikes[0].title().}'
# message = 'my first bike is {}'.format(bikes[0].title())
# print(message)
#
# names = ['abhi','anu','sonu','moni']
#
#
# pop_out = names.pop(0)
# pop_out1 = names.pop(1)
#
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
# print(f"{modified_mem} couldn't attend the dinner")
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
#
# print(m1)
# print(m2)
# print(m3)
#
# # info = ['abhi','anu']
# # # 1.append the list; 2.del item from the list; 3.pop from the list; 4.insert into the list
# #
# # info.append('yashu')
# # print(info)
# # del info[1]
# # print(info)
# # info.pop(0)
# # print(info)
# # info.insert(1,'abhi')
# # print(info)
#
# # cars = ['audi','bmw','duster','ferrari']
# # print(len(cars))
# # print('Here is the original list:')
# # print(cars)
# # print('\n Here is the sorted list:')
# # print(sorted(cars))
# # print(cars)
# # cars.reverse()
# # print(cars)
#
# # places = ['lxpt','mncl','gdk','hyd','rme']
# # print(places)
# # print(sorted(places))
# # print('\n Here is the original list:')
# # print(places)
# # places.reverse()
# # print(places)
# # places.reverse()
# # print(places)
# # places.sort()
# # print(places)
# # foods = ['rice','curry','egg','apple','curd']
# # print(foods)
# # z = foods[0:3]
# # x = foods[1:4]
# # y = foods[-3:]
# # print('\n The first three items in the list are: ')
# # print(z)
# # print('\nThe middle items in the list are: ')
# # print(x)
# # print('\nThe last three items in the list are: ')
# # print(y)
# # my_foods = foods[:]
# # my_foods.append('ice cream')
# # print(my_foods)
# # for food in foods:
# #     print(food)
# # for my_food in my_foods:
# #     print(my_food)
#
#
# ####-- TUPLES --####
#
# # dimensions = (20,30)
# # print('\noriginal dimensions: ')
# # for dimension in dimensions:
# #     print(dimension)
# #
# # dimensions = (40,50)
# # print('\nmodified domentions are: ')
# # for dimension in dimensions:
# #     print(dimension)
#
# # foods = ('pasta','macaroni','zuccini','lasagna')
# # foods[1] = 'cheese'
# # print(foods)
# # print("\nRestaurant's original menu: ")
# # for food in foods:
# #     print(food.title())
# #
# # foods = ('pasta','lasagna')
# # print("\nRestaurant's modified menu: ")
# # for food in foods:
# #     print(food.title())
#
# # cars = ['audi','benz','tata','toyota']
# # if 'audi' in cars:
# #     print('yes its in the cars list')
# #
# # else:
# #     print('Sorry..!')
# # for car in cars:
# #     if car == 'zumba':
# #         print(car.upper())
# #     else:
# #         print(car.title())
#
# # car = 'audi'
#
# # if car != 'zoom':
# #     print('Try again')
#
# ####--IF AND ELSE AND ELIF--####
#
# # age = int(input('Please enter your age: \n'))
# # if age < 4:
# #     price = 20
# #     # print("Adission fee is Rs 20")
# # elif age < 18:
# #     price = 25
# #     # print("admission fee is Rs 25")
# # elif age >=60:
# #     price = 50
# #     # print("admission fee is Rs 50")
# # print(f'Your admission cost is {price}')
#
# # alien_color = 'green'
# #
# # if alien_color == "blue":
# #     print("Player just earned 5 points")
# # else:
# #     print("Player just earned 10 points")
#
# # # alien_color = 'green'
# # alien_color = 'yellow'
# # alien_color = 'red'
# #
# # if alien_color == "green":
# #     print("Player just earned 5 points")
# # elif alien_color == 'yellow':
# #     print("player just earned 10 points")
# # else:
# #     print("Player just earned 20 points")
#
#
# # age = int(input('Please enter your age: \n'))
# # if age < 2:
# #     print("You are a baby.!")
# # elif age >= 2 and age < 4:
# #     print("You are a toddler.!")
# # elif age >= 4 and age < 13:
# #     print("you are a kid.!")
# # elif age >= 13 and age < 20:
# #     print("you are a teenager.!")
# # elif age >= 20 and age < 65:
# #     print("you are an adult.!")
# # else:
# #     print("you are an elder.!")
#
# # fav_fruit = ['apple','mango','grapes','orange','pineapple']
# # if 'apple' in fav_fruit:
# #     print('You really like apple')
# # if 'mango' in fav_fruit:
# #     print("\nyou really like mango")
# # if 'grapes' in fav_fruit:
# #     print("\nyou really like grapes")
# # if 'orange' in fav_fruit:
# #     print("\nyou really like orange")
# # if 'pineapple' in fav_fruit:
# #     print("\nyou really like pineapple")
#
#
# # available_toppings = ['mushroom','olives','green peppers','pepparoni','pineapple','extra cheese']
# # requested_toppings = ['olives','green peppers','mushroom','french fries']
# # for requested_topping in requested_toppings:
# #     if requested_topping in available_toppings:
# #         print(f'adding {requested_topping.title()}')
# #     else:
# #         print(f"sorry we dont have {requested_topping.title()}")
# # print('\nfinished making your pizza')
#
# # if requested_toppings:
# #     for requested_topping in requested_toppings:
# #         print(f'Adding {requested_topping} ')
# #         print('Finished making your pizza')
# # print("\nDo you really need a plain pizza")
#
# # names = ['admin','abhi_h','anu_h','sonu_k']
# # names = []
# # if names:
# #     for name in names:
# #         if name == 'admin':
# #             print("Hello Admin, would you like to see a status report?")
# #         else:
# #             print(f"Hello {name.title()}, thank you for logging in again.!")
# # else:
# #     # print(f"Hello {name}, thank you for logging in again.!")
# #     print("We need to find some users.!")
# # print('\nThank you have a Great day..!')
#
# # current_users = ['abhi_h','anu_h','SONU_K']
# # new_users = ['sonu_k','moni_k','abhi_h','anu_h']
# #
# # for new_user in new_users:
# #     if new_user.lower() in current_users:
# #         print('You need to create a new username'.title())
# #     else:
# #         print('username is available'.title())
#
# # num = [1,2,3,4,5,6,7,8,9]
# # for i in num:
# #     # print(i)
# #     if i == 1 :
# #         print(i,'st')
# #     elif i == 2:
# #         print(i,'nd')
# #     elif i == 3:
# #         print(i,'rd')
# #     else:
# #         print(i,'th')
#
# ###----DICTIONARY----####
#
# # alien_0 = {'color':'green', 'points':5}
# # # print(alien_0['points'])
# # # print(alien_0['color'])
# # print(alien_0)
# # alien_0={}
# # alien_0['x_coordinate']= 0
# # alien_0['y_coordinate'] = 30
# # alien_0['speed']='medium'
# # # print(f"The color of alien is {alien_0['color']}".title())
# # print(f"original-position: {alien_0['x_coordinate']}".title())
# # if alien_0['speed'] == 'slow':
# #     x_increment = 1
# # elif alien_0['speed'] == 'medium':
# #     x_increment = 2
# # else:
# #     x_increment = 3
# # alien_0['x_coordinate']= alien_0['x_coordinate']+ x_increment
# # print(f"new x_position: {alien_0['x_coordinate']}".title())
#
# # name = "s3://amazon.com"
# # def get_name(name:str):
# #     not_name = False
# #     not_namee = False
# #     name1 = 's3://aws.com'.lower()
# #     if name[:len(name1)].lower()!= name1:
# #         not_name = True
# #     name2 = 'hariii'.lower()
# #     if name[:len(name2)].lower()!= name2:
# #         not_namee = True
# #     if not_name and not_namee:
# #         name = 'H'+ name
# #     # if (not_namee == False):
# #     #     name = "a"+ name
# #         return name
# # print(get_name("satya"))
#
# # DICTIONARY GET
#
# # name = {'abhi':'hari','anu':'hari'}
# # # print(name['satya'])
# # print_value = name.get('satya','No key_value for the key = satya')
# # print(print_value)
# # details = {
# #     'name':'abhi',
# #     'lname':'hari',
# #     'age':30,
# #     'address':'Hyderabad'
# # }
# # print(details)
# # print(details['name'])
# # print(details['lname'])
# # print(details['age'])
# # print(details['address'])
#
# # for i in details:
# #     print(i,':',details[i])
# # for i,j in details.items():
# #     print(i,':',j)
#
# # user = {
# #     'username': 'abhi',
# #     'first':"a",
# #     'last':'H'
# # }
# # for key,value in user.items():
# #     print(f'\nkey:{key}')
# #     print(f'value:{value}')
#
# # fav_languages = {
# #     'abhi':'python',
# #     'anu':'java',
# #     'satya':'javascript'
# # }
# # for name,language in fav_languages.items():
# #     print(f"{name.title()}'s fav language is {language}.")
# # friends = ['abhi','anu']
# # for name in fav_languages.keys():
# #     print(f'Hi {name.title()}')
# #
# #     if name in friends:
# #         language = fav_languages[name].title()
# #         print(f'\t{name.title()},I see you love {language}')
# # if 'moni' not in fav_languages.keys():
# #     print('Moni please take a poll')
#
# # for name in sorted(fav_languages.keys()):
# #     print(f'{name.title()}. Thank you for taking the poll')
#
# # details = {
# #     'name':'abhi',
# #     'lname':'hari',
# #     'age':30,
# #     'address':'Hyderabad'
# # }
# #
# # for key,value in details.items():
# #     print(f'{key}:{value}')
#
# # dict = {
# #     'delhi':'hyd',
# #     'hyd':'telangana',
# #     'raksha':'hyd'
# # }
#
# # for key,value in dict.items():
# #     print(f'{key.title()} is the capital of {value.title()}')
# # for key in dict.keys():
# #     print(f'{key.title()}')
# #
# # for value in dict.values():
# #     print(f'{value.title()}')
#
# # fav_languages = {
# #     'abhi':'python',
# #     'anu':'java',
# #     'satya':'javascript'
# # }
# # friends = ['satya','moni','abhi','anu','sonu']
# #
# # for i in friends:
# #     if i in fav_languages.keys():
# #         print(f'{i.title()}. Thanks for taking the poll')
# #     else:
# #         print(f'{i.title()} Sorry, You need to take the poll')
#
#
# ####----NESTED-DICT----####
#
# # friends = {'color':'Green','speed':'Slow','points':5}
# # friends2 = {'color':'Yellow','speed':'Slow','points':15}
# # friends3 = [friends,friends2]
# # print(friends3)
#
# # dict = []
# #
# # for dict_num in range(5):
# #     new_dict = {'name':'abhi','age':30}
# #     dict.append(new_dict)
# #     # print(dict)
# # for i in dict[:3]:
# #     print(dict)
# # print('.....')
# # print(f'\nTotal number of aliens added {len(dict)}')
#
# # for i in dict[:2]:
# #     if i['name'] == 'abhi':
# #         i['name'] = 'Abhinay'
# #         i['age'] = 29
# #         print(dict)
#
# # pizza = {
# #     'crust':'thick',
# #     'toppings':['mushrooms','pepparoni']
# # }
# # print(f"You have ordered a {pizza['crust']}-crust pizza With the toppings:")
# # print('')
# # for topping in pizza['toppings']:
# #     print('\t'+ topping)
#
# # favorite_languages = {
# #     'jen': ['python', 'ruby'],
# #     'sarah': ['c'],
# #     'edward': ['ruby', 'go'],
# #     'phil': ['python', 'haskell'],
# # }
# # for name,languages in favorite_languages.items():
# #     print(f"\n{name.title()}'s favourite languages are: ")
# #     for language in languages:
# #         print(f'\t{language.title()}')
#
# # favorite_languages = {
# #     'Abhi': ['python'],
# #     'Anu': ['c','Java'],
# #     'edward': ['ruby'],
# #     'phil': ['python', 'haskell'],
# # }
# #
# # for name,languages in favorite_languages.items():
# #     if len(languages)<=1:
# #         print(f"{name.title()}'s fav language is: ")
# #     else:
# #         print(f"{name.title()}'s fav languages are: ")
# #     for language in languages:
# #         print(f"\t{language.title()}")
#
# # users = {
# #     'abhi':{
# #         'fname':'Hari',
# #         'lname':'Abhi',
# #         'age':30
# #     },
# #     'anu':{
# #         'fname':'Hari',
# #         'lname':'Anu',
# #         'age':28
# #     },
# #     'satya':{
# #         'fname':'Hari',
# #         'lname':'Satya',
# #         'age':27
# #     }
# # }
# # for username,user_info in users.items():
# #     print(f"\nusername:{username}")
# #     full_name = f"{user_info['fname']} {user_info['lname']}"
# #     age = f"{user_info['age']}"
# #
# #     print(f"\tfull_name = {full_name.title()}")
# #     print(f"\tAge= {age.title()}")
# #
# # for name,info in users.items():
# #     print(f"username = {name}")
# #     full_name = f"{info['fname']}-{info['lname']}"
# #     age = f"{info['age']}"
# #
# #     print(f"\tFullname = {full_name}")
# #     print(f"\tAge = {age}")
#
# # user1 = {
# #     'name':'abhi',
# #     'age':30
# # }
# # user2 = {
# #     'name':'anu',
# #     'age':28
# # }
# #
# # people = [user1,user2]
# # print(people)
# # for i in people:
# #     print(f"{i['name']} {i['age']}")
#
# # pet = {
# #     'name':'DOG',
# #     'nature':'faithful',
# #     'owner': 'abhi'
# # }
# # owner = {
# #     'name':'cat',
# #     'nature':'cunning',
# #     'owner':'anu'
# # }
# # pets = [pet,owner]
# # print(pets)
# #
# # for i in pets:
# #     print(f"A {i['name'].title()} is a {i['nature']} and its owner is {i['owner'].title()}")
#
# ####----INPUT AND WHILE_LOOP----####
#
# # rental_car = input("What kind of rental car you would like?\n")
# # print(f"let me find you a {rental_car}")
# # question = input("How many people are in your dinner group?\n ")
# # question = int(question)
# # if question >8:
# #     print("I am sorry you need to wait for the table to get ready..!")
# # else:
# #     print("Your table is ready.!")
#
# # ten = int(input("Enter a number: \n"))
# # if ten % 10 ==0:
# #     print(f"{ten} is the multiple of 10.!")
# # else:
# #     print(f"{ten} is not the multiple of 10.!")
#
# # prompt = "Tell me something to do i will repeat it for you:"
# # prompt+= "\nEnter 'quit to end the program"
# #
# # message = ''
# # while message!= 'quit':
# #     message = input(prompt)
# #     if message!='quit':
# #         print(message)
#
# # message = int(input("Enter a number: \n"))
# # curr_num = 1
# #
# # while curr_num<=6:
# #     print(curr_num)
# #     curr_num+=1
# # prompt = "Tell me what to do i will do it for u"
# # prompt ="Enter 'quit to end the program"
# # active = True
# # message = ''
# # while active:
# #     message = input(prompt)
# #
# #     if message == 'quit':
# #         active = False
# #     else:
# #         print(message)
#
# # curr_num = int(input("enter a number: \n"))
#
# # while curr_num<=6:
# #     print(curr_num)
# #     curr_num+=1
# # while curr_num < 10:
# #     curr_num+=1
# #     if curr_num  == 3:
# #         continue
# #     else:
# #         print(curr_num)
#
# # 1.ask user to enter a series of pizza topping till they enter 'quit'
# # 2.print a message saying we are adding the topping to their pizza
#
# # prompt = "Please enter your topping:"
# # prompt += "\nEnter 'quit' to end the program"
#
#
# # while message!='quit':
# #     message = input(prompt)
# #     if message!='quit':
# #         print(f"We are adding {message} to your pizza..!")
# # active = True
# # message = ""
# # while active:
# #     message = input(prompt)
# #     if message == 'quit':
# #         active = False
# #     else:
# #         print(f"We are adding {message} to your pizza..!!")
#
# # 1.age <3 fare is free
# # 2. age >=3 and age <12 fare is 10$
# # 3.age > 12 fare is 15$
# # 4.ask theirs age and print the fare
#
# # age = int(input("Please enter your age: "))
# # while True:
# #     if age < 3:
# #         print("Your fare for the ticket is free")
# #         break
# #     elif age >=3 and age <12:
# #         print("Your fare for the ticket is 10$")
# #         break
# #     else:
# #         print("Your fare for the ticket is 15$")
# #         break
#
# ####----WHILE_LOOP WITH LISTS AND DICTIONARIES----####
#
# # unconfirmed_users = ['abhi','anu','sonu','moni']
# # confirmed_users = []
#
# # while unconfirmed_users:
# #     current_user = unconfirmed_users.pop()
# #
# #     print(f"Verifying user: {current_user.title()}")
# #     confirmed_users.append(current_user)
# # print("\nThe following users have been confirmed:")
# # for confirmed_user in confirmed_users:
# #     print(confirmed_user.title())
#
# # pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# # print(pets)
# #
# # while 'cat' in pets:
# #     pets.remove('cat')
# # print(pets)
#
# # responses = {}
# # polling_active = True
# # while polling_active:
# #     name = input("\nwhat is your name?")
# #     response = input(("\nWhich mountain would you like to climb someday?"))
# #
# #     responses[name] = response
# #
# #     repeat = input(("Would you like to ley other people respond? (y or n)"))
# #
# #     if repeat == 'n':
# #         polling_active = False
# # print("\n---Polling results----")
# # for name,response in responses.items():
# #     print(f"{name} would like to climb {response} someday")
#
# # """TRI IT YOURSELF"""
#
# # 1.Empty dict
# # 2.append the empty dict
# # 3.Ask where they like other people to take the poll
# # 4.Print the polling results
#
# # poll = {}
# # polling_active = True
# # while polling_active:
# #     name = input("What is your name?\n")
# #     response = input("Which mountain would you like to climb one day?\n")
# #
# #     poll[name] = response
# #
# #     repeat = input("would you like to let other people take the poll? (y or n)")
# #     if repeat == 'n':
# #         polling_active = False
# # print("----polling results----")
# #
# # for name,response in poll.items():
# #     print(f"{name} would like to climb {response} one day..!")
#
# # sandwich_orders = ['pastrami','fish','tuna','pastrami','veg','pastrami']
# # finished_sandwiches = []
# # print("Deli has run out of 'pastrami'")
# # while 'pastrami' in sandwich_orders:
# #     sandwich_orders.remove('pastrami')
# #     print(sandwich_orders)
# # for sandwich_order in sandwich_orders:
# #     print(f"I made your {sandwich_order} sandwich")
# #     finished_sandwiches.append(sandwich_order)
# # print("--SANDWICHES MADE--")
# # for finished_sandwich in finished_sandwiches:
# #     print(f"{finished_sandwich}")
# # print(finished_sandwiches)
#
# # people = {}
# #
# # polling_active = True
# #
# # while polling_active:
# #     name = input("Please enter your name: \n")
# #     question = input("If you could visit one place in the world, where would you go?\n")
# #
# #     people[name] = question
# #
# #     repeat = input("Would you let others take the poll? (y or n)")
# #     if repeat == 'n':
# #         polling_active = False
# # print("----POLL RESULTS----")
# # for name,question in people.items():
# #     print(f"{name} would like to visit {question} in the world..!")
#
# ####----FUNCTIONS----####
#
# # def greet_user():
# #     """Display a simple greeting message """
# #     print("Hello")
# # greet_user()
# #
# # """passing username to a function"""
# #
# # def greet_user(username):
# #     print(f"Hello {username}")
# # greet_user('Abhi')
#
# # def display_message():
# #     print("I am learning 'Functions' in this chapter")
# # display_message()
#
# # def fav_book(title):
# #     print(f"My fav book is {title}".title())
# # fav_book("Alice the wonderland")
#
# # def describe_pet(animal_type,petname):
# #     """Describe the pet info"""
# #     print(f"\nI have a {animal_type}".title())
# #     print(f"My {animal_type}'s name is {petname}")
# # describe_pet('dog','Browney')
# # describe_pet('cat','smiley')
#
# # def make_shirt(message,size = 'L'):
# #     print(f"The Size of the T_shirt is {size} with the message {message}")
# # make_shirt('I LOVE PYTHON')
# # """With key word arguments"""
# # make_shirt(size='L',message='PYTHON DEVELOPER')
#
# # def make_shirt(size,message = 'PYTHON IS LOVE..'):
# #     print(f"The Size of the T_shirt is {size} with the message:{message}")
# # make_shirt('M')
#
# # def describe_city(city,country = 'India'):
# #     print(f"{city} is in {country}")
# # describe_city('Hyderabad')
# # describe_city('Lxpt')
# # describe_city('Knr')
#
# # def get_foratted_one(fname,lname,mname):
# #     """Return a full name, neatly formatted"""
# #     full_name = f"{fname} {mname} {lname}"
# #     return full_name.title()
# #
# # musician = get_foratted_one('Hari','','Abhi')
# # print(musician)
#
# # def get_foratted_one(fname,lname,mname= ''):
# #     """Return a full name, neatly formatted"""
# #     if mname:
# #         full_name = f"{fname} {mname} {lname}".title()
# #     else:
# #         full_name = f'{fname} {lname}'.title()
# #     return full_name.title()
# #
# # musician = get_foratted_one('Hari','Mr','Abhi')
# # print(musician)
#
# # def build_person(fname,lname,age = None):
# #     person = {'first':fname,'last':lname}
# #     if age:
# #         person['age'] = age
# #     return person
# #
# # details = build_person('Hari','Abhi', age=30)
# # print(details)
#
# # def get_foratted_one(fname,lname):
# #     """Return a full name, neatly formatted"""
# #     full_name = f"{fname} {lname}"
# #     return full_name.title()
#
#
#                 # """TRY IT YOURSELF"""
#
# # def city_country(city,country):
# #     details = f"{city},{country}".title()
# #     return details
# # # city_country('hyderabad','India')
# # info = city_country('gdk','india')
# # info1 = city_country('Hyd','india')
# # info2 = city_country('knr','india')
# # print(info)
# # print(info1)
# # print(info2)
#
# # def make_album(artist_name,album_title):
# #     details ={'name':artist_name,'title':album_title}
#     # return details
#
# # dict = make_album(123,45)
# # dict2 = make_album(456,789)
# # dict3 = make_album(4567,7892)
# #
# # print(dict)
# # print(dict2)
# # print(dict3)
#
# # def make_album(artist_name,album_title,no_of_songs=None):
# #     details ={'name':artist_name,'title':album_title}
# #
# #     """With none to add extra parameter in the dict"""
# #     if no_of_songs:
# #         details['no_of_songs'] = no_of_songs
# #         return details
# #
# # dict = make_album(123,456,8)
# # print(dict)
#
# # def make_album(artist_name,album_title):
# #     details ={'name':artist_name,'title':album_title}
# #     return details
# # while True:
# #     print("\nEnter artist details: ")
# #     print("Enter 'q' anytime to quit")
# #     name = input("Enter Artist's name: ")
# #     # title = input("Enter Album's title: ")
# #
# #     if name =='q':
# #         break
# #     title = input("Enter Album's title: ")
# #     if title == 'q':
# #         break
# #     dict = make_album(name,title)
# #     print(f"The {name} has the {title} album".title())
# """Practice 'quit' """
#
# # def make_list(name,title):
# #     person = {'artist_name':name,'album_title':title}
# #     return person
# #
# # while True:
# #     print("\nEnter INFO")
# #     print("Enter 'q' anytime to quit")
# #     artist_name = input("Enter Name: ")
# #     if artist_name == 'q':
# #         break
# #     album_title = input("Enter title: ")
# #     if album_title == 'q':
# #         break
# #     details = make_list(artist_name,album_title)
# #     print(f"{artist_name} has {album_title} title records".title())
#
#                 # """PRACTICE"""
#
# # def greeting(names):
# #     """Print a greeting to each user in the list"""
# #     for name in names:
# #         print(f"Hello {name}".title())
# # usernames = ['Abhi','Anu','Hari']
# # greeting(usernames)
#
# # unprinted_designs = ['phone case','robot','pencil']
# # completed_designs = []
# #
# # # Simulate printing each design, until none are left.
# # # Move each design to completed_models after printing.
# #
# # while unprinted_designs:
# #     current_design = unprinted_designs.pop()
# #
# #     print(f"printing models: {current_design}")
# #     completed_designs.append(current_design)
# #
# # # Display all completed models.
# # print("\nThe following models have been printed:")
# # for completed_design in completed_designs:
# #     print(completed_design)
#
# """printing models using 'functions' """
#
# # def printing_model(unprinted_design,completed_models):
# #
# #     while unprinted_design:
# #         current_model = unprinted_design.pop()
# #         print(f"Printing models: {current_model}")
# #         completed_models.append(current_model)
# #
# # def show_completed_models(completed_models):
# #     print("\nThe following models have been printed: ")
# #     for completed_model in completed_models:
# #         print(completed_model)
# #
# # unprinted_models = ['rubber','pencil','pen']
# # unprinted_design = unprinted_models[:]
# # completed_models = []
# #
# # printing_model(unprinted_models,completed_models)
# # show_completed_models(completed_models)
#
# # print(unprinted_design)
#
# #               TRY IT YOURSELF
#
# # def show_messages(names):
# #     for name in names:
# #         print(f"Hello {name}".title())
# #
# # list = ['Abhi', 'anu', 'satya']
# # show_messages(list)
#
# # def show_messages(names,sent_messages):
# #     print("\nThe following names have been moved: ")
# #     while names:
# #         sending_messages = names.pop()
# #         print(f"Hello {sending_messages}")
# #         sent_messages.append(sending_messages)
# #
# # def send_messages(sent_messages):
# #     print("\nThe moved messages are: ")
# #     for send_message in sent_messages:
# #         print(send_message)
# # list = ['Abhi', 'anu', 'satya']
# # sent_messages = []
# # show_messages(list,sent_messages)
# # send_messages(sent_messages)
# # print(sent_messages)
# # print(list)
#
#
# # def show_messages(list_copied,sent_messages):
# #     print("\nThe following messages have been moved: ")
# #     while list_copied:
# #         sending_messages = list_copied.pop()
# #         print(f"{sending_messages}")
# #         sent_messages.append(sending_messages)
# #
# # def send_messages(sent_messages):
# #     print("\nThe moved messages are: ")
# #     for send_message in sent_messages:
# #         print(send_message)
# # list = ['Hello Abhi', 'Hello anu', 'Hello satya']
# # list_copied = list[:]
# # sent_messages = []
# #
# # show_messages(list_copied,sent_messages)
# # send_messages(sent_messages)
# #
# # print(sent_messages)
# # print(list)
#
#
# # def pizza(*toppings):
# #     print(toppings)
# # # toppings = ['a','b','c']
# # pizza('a')
# # pizza('a','b','c','d')
#
# # def pizza(*toppings):
# #     print("\nMaking a pizza with the following toppings")
# #     for topping in toppings:
# #         print(f"-{topping}")
# # pizza('mushroom','pepparoni','cheese')
#
# # def making_pizza(size,*toppings):
# #     print(f"\nMaking a {size} inch pizza with the following toppings:")
# #     for topping in toppings:
# #         print(f"-{topping}")
# # making_pizza(10,'mushroom')
# # making_pizza(12,'pepparoni','extra cheese')
#
# # def make_profile(fname,lname,**user_info):
# #     user_info['first_name'] = fname
# #     user_info['last_name'] = lname
# #     return user_info
# # profile = make_profile('hari','abhi',location = 'Hyderabd',field = 'Computers')
# # # make_profile('hari','abhi',location = 'Hyderabd',field = 'Computers')
# # print(profile)
#
# # def make_sandwich(*items):
# #     print("\nMaking sandwich with the list of items: ")
# #     for item in items:
# #         print(f"-{item}")
# # make_sandwich('cheese')
# # make_sandwich('hot','olive','tomato')
# # make_sandwich('empty')
#
# # def make_profile(fname,lname,**details):
# #     details['firstname'] = fname
# #     details['lastname'] = lname
# #     return details
# # person = make_profile('hari','abhi',location = 'hyderabad',field = 'ECE',uniersity = 'JNTU')
# # print(person)
#
# # def car_details(car,type,**info):
# #     # print('\nDetails are: ')
# #     info['Name'] = car
# #     info['Type'] = type
# #     return info
# # details = car_details('Terrano','SUV',maker = 'Nissan')
# # details2 = car_details('Maruti 800','mini',maker = 'Maruti',wheelbase = 'small')
# # print(details)
# # print(details2)
#
# #                                   ----CLASSES----
#
# # class dog:
# #     """A simple attempt to model a dog"""
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #
# #     def sit(self):
# #         """simulate a dog sitting in response to a command"""
# #         print(f"{self.name} is now sitting")
# #
# #     def roll_over(self):
# #         """simulate rolling over in response to a command"""
# #         print(f"{self.name} is rolled over")
# #
# # my_dog = dog('browney',6)
# # print(f"My dog name is {my_dog.name}")
# # print(f'My dog age is {my_dog.age}')
# # my_dog.sit()
# # my_dog.roll_over()
# #
# # your_dog = dog('Snoopy',5)
# # print(f"\nMy dog name is {your_dog.name}")
# # your_dog.sit()
# # your_dog.roll_over()
#
# class restaurent:
#     def __init__(self,name,cusine):
#         self.name = name
#         self.cusine =cusine

#     def describe_restaurent(self):
#         print(f"\nName of the restaurent is {self.name}")
#         print(f"Cusine type of the restaurent is {self.cusine}")

#     def open_restaurent(self):
#         print(f"{self.name} is now Open..!")
# #
# # Restaurent = restaurent('My_restaurent','Indian')
# # print(f"{Restaurent.name} is a good choice..! Because it has {Restaurent.cusine} cusine. ")
# # Restaurent.describe_restaurent()
# # Restaurent.open_restaurent()
#
# # abhi = restaurent('AH','Italian')
# # anu = restaurent('AN','Indian')
# # satya = restaurent('VS','Home-Made')
# #
# # abhi.describe_restaurent()
# # anu.describe_restaurent()
# # satya.describe_restaurent()
#
# # class user:
# #
# #     def __init__(self,fname,lname,age,location):
# #         self.fname = fname
# #         self.lname = lname
# #         self.age = age
# #         self.location = location
# #
# #     def describe_user(self):
# #         print(f"\nHi my name is {self.fname} {self.lname}")
# #         print(f"I am {self.age} years old")
# #         print(f'I stay in {self.location}')
# #
# #     def greet_user(self):
# #         print(f"\nHello {self.fname} {self.lname}. Welcome..!!")
# #
# # abhi = user('Hari','Abhinay',30,'Ind')
# #
# # abhi.describe_user()
# # abhi.greet_user()
# #
# # anu = user('Hari','Anurag',28, 'India')
# # anu.describe_user()
# # anu.greet_user()
#
#
# # class Car:
# #
# #     def __init__(self,name,model,year):
# #         self.name = name
# #         self.model = model
# #         self.year = year
# #         self.mileage = 60
# #
# #     def describe_car(self):
# #         long_name = f'{self.year} {self.model} {self.name}'
# #         return long_name
# #
# #     def car_mileage(self):
# #         print(f"This car has {self.mileage} miles on it.")
# #
# #     def update_mileage(self,mileage):
# #         if mileage >= self.mileage:
# #             self.mileage = mileage
# #         else:
# #             print("You cant roll back the Mileage..!")
# #
# #     def increment_odometer(self,miles):
# #         self.mileage+=miles
# #
# # my_car = Car('Maruti','Maruti 800', 2014)
# # print(my_car.describe_car())
# # # my_car.mileage = 50
# # my_car.update_mileage(59)
# # my_car.car_mileage()
# # my_car.increment_odometer(1000)
# # my_car.car_mileage()
#
# # class restaurent:
# #     def __init__(self,name,cusine):
# #         self.name = name
# #         self.cusine =cusine
# #         self.number_served = 25
# #
# #     def describe_restaurent(self):
# #         print(f"\nName of the restaurent is {self.name}")
# #         print(f"Cusine type of the restaurent is {self.cusine}")
# #
# #     def open_restaurent(self):
# #         print(f"{self.name} is now Open..!")
# #
# #     def set_number_served(self):
# #         print(f"The number of customers served are: {self.number_served}")
# #
# #     def increment_num_served(self,Add):
# #         self.number_served+=Add
# #
# #
# # Restaurant = restaurent("Abhi","Indian")
# # Restaurant.set_number_served()
# # Restaurant.increment_num_served(5)
# # Restaurant.set_number_served()
#
# # class user:
# #
# #     def __init__(self,fname,lname):
# #         self.fname = fname
# #         self.lname = lname
# #         # self.age = age
# #         # self.location = location
# #         self.login_attempts = 0
# #
# #     def describe_user(self):
# #         print(f"\nHi my name is {self.fname} {self.lname}")
# #         # print(f"I am {self.age} years old")
# #         # print(f'I stay in {self.location}')
# #
# #     def greet_user(self):
# #         print(f"\nHello {self.fname} {self.lname}. Welcome..!!")
# #
# #     def Login_attempts(self):
# #         print(f"The login attempts are: {self.login_attempts}")
# #
# #     def increment_login_attempts(self):
# #         self.login_attempts+=1
# #
# #     def reset_login_attempts(self):
# #         if self.login_attempts !=0:
# #             self.login_attempts =0
# #         else:
# #             self.login_attempts = self.login_attempts
# #
# # people = user('Hari','Abhi')
# # people.describe_user()
# # people.greet_user()
# # people.increment_login_attempts()
# # people.increment_login_attempts()
# # people.increment_login_attempts()
# # # people.Login_attempts()
# # people.increment_login_attempts()
# # people.Login_attempts()
# # people.reset_login_attempts()
# # people.Login_attempts()
# # people.increment_login_attempts()
# # people.Login_attempts()
# # people.increment_login_attempts()
# # people.increment_login_attempts()
# # people.Login_attempts()
# # people.reset_login_attempts()
# # people.Login_attempts()
# # people.increment_login_attempts()
# # people.Login_attempts()
#
# # class Car:
# #     def __init__(self,name,model,year):
# #         self.name = name
# #         self.model = model
# #         self.year = year
# #         self.mileage = 60
# #         self.fuel = 50
# #
# #     def describe_car(self):
# #         long_name = f'{self.year} {self.model} {self.name}'
# #         return long_name
# #
# #     def fuel_tank(self):
# #         print(f"This car has {self.fuel}-litre capacity")
# #
# # class Battery:
# #     def __init__(self,battery_size = 100):
# #         self.battery_size = battery_size
# #
# #     def describe_battery(self):
# #         print(f"This car has {self.battery_size}-KHW battery")
# #
# #     def get_range(self):
# #         # global range
# #         if self.battery_size == 80:
# #             range = 250
# #         elif self.battery_size == 100:
# #             range = 350
# #
# #         print(f"This car can go about {range} kms on full charge")
# #
# #
# #
# # class electronic_car(Car):
# #
# #     def __init__(self,name,model,year):
# #         super().__init__(name,model,year)
# #         self.battery = Battery()
# #
# #     # def battery_size(self):
# #     #     print(f"This car has {self.battery} khw battery")
# #
# #     def fuel_tank(self):
# #         print("This car doesnt need a gas tank.")
# #
# #
# # details= electronic_car('tesla','elect',2010)
# # print(details.describe_car())
# # details.fuel_tank()
# # details.battery.describe_battery()
# # details.battery.get_range()
#
# #                       TRY IT YOURSELF
# # class restaurent:
# #     def __init__(self,name,cusine):
# #         self.name = name
# #         self.cusine =cusine
# #
# #     def describe_restaurent(self):
# #         print(f"\nName of the restaurent is {self.name}")
# #         print(f"Cusine type of the restaurent is {self.cusine}")
# #
# # class icecream_stand(restaurent):
# #
# #     def __init__(self,name,cusine):
# #         super().__init__(name,cusine)
# #     def display_flavors(self):
# #         flavor = ['vanila','strawberry','chocolate']
# #         print("\nThe flavors we have are: ")
# #         for flavors in flavor:
# #             print(f"{flavors}")
# #
# #
# # detail = icecream_stand('Abhi','Ind')
# # detail.describe_restaurent()
# # detail.display_flavors()
#
#
# # class user:
# # #
# #     def __init__(self,fname,lname,age,location):
# #         self.fname = fname
# #         self.lname = lname
# #         self.age = age
# #         self.location = location
# #
# #     def describe_user(self):
# #         print(f"\nHi my name is {self.fname} {self.lname}")
# #         print(f"I am {self.age} years old")
# #         print(f'I stay in {self.location}')
# #
# #     def greet_user(self):
# #         print(f"Hello {self.fname} {self.lname}. Welcome..!!")
# #
# from User_module import user
# class admin(user):

#     def __init__(self,fname,lname,age,location):
#         super().__init__(fname,lname,age,location)
#         self.privilege = Privilege()
# class Privilege:
#     def show_privileges(self):
#         privileges = ['can add post','can delete post','can ban user']
#         print("\nThe admin privilages are: ")
#         for privilege in privileges:
#             print(f"{privilege}".title())
# #
# # users = admin('Hari','Abhi',29,'Ind')
# # users.greet_user()
# # users.describe_user()
# # # users.show_privileges()
# # users.privilege.show_privileges()
#
#
# class Car:
#     def __init__(self,name,model,year):
#         self.name = name
#         self.model = model
#         self.year = year
#         self.mileage = 60
#         self.fuel = 50
#         self.battery = Battery()

#     def describe_car(self):
#         long_name = f'{self.year} {self.model} {self.name}'
#         return long_name
#     def fuel_tank(self):
#         print(f"This car has {self.fuel}-litre capacity")
# class Battery:
#     def __init__(self,battery_size = 80):
#         self.battery_size = battery_size
#     def describe_battery(self):
#         print(f"This car has {self.battery_size}-KHW battery")
#     def get_range(self):
#         # global range
#         if self.battery_size == 80:
#             range = 250
#         elif self.battery_size == 100:
#             range = 350

#         print(f"This car can go about {range} kms on full charge")

#     def upgrade_battery(self):
#         if self.battery_size == self.battery_size:
#             self.battery_size = 100
#         # else:
#         #     self.battery_size = self.battery_size
# class electronic_car(Car):

#     def __init__(self,name,model,year):
#         super().__init__(name,model,year)
#         self.battery = Battery()

#     # def battery_size(self):
#     #     print(f"This car has {self.battery} khw battery")
#     def fuel_tank(self):
#         print("This car doesnt need a gas tank.")


# details= electronic_car('tesla','elect',2010)
# print(details.describe_car())
# details.fuel_tank()
# details.battery.describe_battery()
# details.battery.get_range()
# details.battery.upgrade_battery()
# details.battery.get_range()

# roll a dice 10 times
# from random import randint
# class die:
#     # dice_list = []
#     def __init__(self,sides):
#         self.sides = sides

#     def roll_die(self,times):
#         dice_list = []
#         times=0
#         while True:
#             # if times:
#             number = randint(1,self.sides)
#             times+=1
#             print(f"Number is : {number}",times)
#             dice_list.append(number)
#             if times == 10:
#                 print(dice_list)
#                 break

# det = die(30)
# det.roll_die(10)

"""This code is not finished yet. I will work on it later"""
# from random import choice
# list = [1,2,3,4,5,6,7,8,9,10,'q','w','e','r']
# matching_ticket = []
# my_ticket = ['q','r',1,'w']
# while len(matching_ticket)<4:
#     pulled_item = choice(list)

#     if pulled_item not in matching_ticket:
#         print(f"we pulled a: {pulled_item}")
#         matching_ticket.append(pulled_item)
    
#     if matching_ticket == my_ticket:
#         print("The number of loops it took to win a lottery: ")
# print("Any ticket mathing this ticket number wins a lottery: ",matching_ticket)


# with open('test_file.txt') as file:
#     data = file.read()
# print(data.rstrip())

# file_path = 'C:/Users/abhih/.vscode/Test1.txt'

# with open (file_path) as file:
#     for line in file:
#         print(line)
# print(data.rstrip)

