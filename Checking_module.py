# from Crash_course import describe_pet
# if __name__ == '__main__':
#     describe_pet('dog','Snoopy')

# from Crash_course import get_foratted_one
#
# while True:
#     print("\nWhat is Your name?")
#     fname = input("first name: ")
#     lname = input("last name: ")
#
#     person = get_foratted_one(fname,lname)
#     print(f"Hello {person}")

# from Crash_course import printing_model
# from Crash_course import show_completed_models
#
# unfinished = ['he','she','it','they']
# finished = []
#
# printing_model(unfinished,finished)
# show_completed_models(finished)

# from Crash_course import car_details
# info = car_details(800,'mini',maker = 'maruti')
# print(info)

# import Crash_course
# det = Crash_course.car_details('Terrano','SUV',maker = 'Nissan',wheelbase = 'Large')
# print(det)


# from Crash_course import car_details as c
#
# inf = c(800,'mini',maker = 'maruti')
# print(inf)

# import Crash_course as cr
#
# dete = cr.car_details(800,'mini',maker = 'maruti',whelbase = 'small')
# print(dete)

# from Crash_course import *
# fun = car_details(800,'mini',maker = 'maruti')
# print(fun)

# from Crash_course import Car as c,electronic_car
#
# # details = c("Tesla",'EV',2020)
# detail = electronic_car("Tesla",'EV',2020)
# # print(details.describe_car())
# detail.battery.describe_battery()

# from Crash_course import restaurent as r
#
# det = r("Abhi","Indian")
# det.describe_restaurent()
# det.open_restaurent()

# from User_module import user
# from Crash_course import admin,Privilege

# details = admin("Hari","Abhi",30,"Ind")
# details.privilege.show_privileges()
#
# det = admin("Hari","Abhi",30,"Ind")
# det.describe_user()
# det.greet_user()
# det.privilege.show_privileges()

# from Crash_course import get_formatted_name

# # prompt = "Enter 'q' to quit"
# while True:
#     prompt = "Enter 'q' to quit"
#     first = input("Enter your first name:\n")
#     if first == 'q':
#         break
#     second = input("Enter last name:\n")
#     if second == 'q':
#         break

#     formatted_name = get_formatted_name(first,second)
#     print(f"Your full name is: {formatted_name}"

from Crash_course import survey,employee

question = "What are the names of your fav car brands?"
my_survey = survey(question)

my_survey.show_question()

while True:
    prompt = "Enter 'q' anytime to quit\n"
    response = input("Brands: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("Thank you for your time")
my_survey.show_results()

