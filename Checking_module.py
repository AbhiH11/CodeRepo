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

from Crash_course import printing_model
from Crash_course import show_completed_models

unfinished = ['he','she','it','they']
finished = []

printing_model(unfinished,finished)
show_completed_models(finished)
