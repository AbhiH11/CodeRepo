#x = 25
#try:
 #   print(x)
#except NameError:
 #   print("variable x is not defined")
#except:
 #   print("something else went wrong")


#try:
 #   print("hello")
#except:
 #   print("something went wrong")
#else:
 #   print("nothing went wrong")

#finally:
    #print("The try except is finished ")



#try:
 #   print("Hello")

#except NameError:
 #   print("variable x is not defined")
#except:
 #   print("Nothing went wrong")
#except:
 #   print("Something went wrong")
#else:
 #   print("Something went wrong")

#finally:
    #print("The except is finished ")


#x = -1
#if x < 0:
 #   raise Exception("Sorry, No numbers below zero")


x = "hello"
if not type(x) is int:
    raise TypeError("Only intergers are allowed")
