#import time
#                                  python time module
# ******************************************************************************
# print(time.ctime(0)) - converts a time expressed in secondes since epoch to a readable string
#                        epoch = when your computer thinks the time began (reference point)
# print(time.time()) return current seconds since epoch
# print(time.ctime(time.time())) will get current time
# ******************************************************************************

# print(help(time))
# time.strftime(format,time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
#time_object = time.gmtime() # UTC time
#print(time_object)
# local_time = time.strftime("%B $d %Y %H:%M:%S", time_object)
# print(local_time)
# *******************************************************************************
# epoch = a date and time from which a computer measures system time
#print(time.ctime(0))
#python #time #module

# ***************************************************************************
#import time
# ***************************************************************************
#print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
#print(time.time())      # return current seconds since epoch
#print(time.ctime(time.time())) # will get current time

# ***************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# ***************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*_*-*-*-*-*-*
# ----------------------------------------------beware-----------------------------------------------------
# robotic agents and AI agents are surviving by repressing and suppressing
# the other species on the planet. Robots needs electricity to survive
# in order to generate electricity environment polution has been must. Environment polution push most other
# species to extinction.(I have written this lines because while learning to code I suddenly came across this idea)
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*_*-*-*-*-*-*
             


#              Python Multithreading
# ******************************************************
# Python threading tutorial
# ******************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

"""import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast.")
def drink_water():
    time.sleep(4)
    print("You drank water.")

def study():
    time.sleep(5)
    print("You study routinely. ")

x = threading.Thread(target = eat_breakfast, args = ())
x.start()
y = threading.Thread(target = drink_water, args = ())
y.start()
z = threading.Thread(target = study, args = ())
z.start()

x.join()
y.join()
z.join()

#eat_breakfast()
#drink_water()
#study()
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
"""

# Python       Deamon Threads
# ************************************************************
# Python daemon threads
# ************************************************************

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for :",count , "seconds")

x = threading.Thread(target = timer, daemon = True)
x.start()

answer = input("Do you wish to exit? : ")





