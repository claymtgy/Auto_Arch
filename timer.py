from random_input_generator import randomizer
from control_timer import RepeatedTimer
from time import sleep

def hello(name):
    print("Hello %s!" % name)

def Timer_Start():
    print("starting...")
    rt = RepeatedTimer(1, hello, "World") # it auto-starts, no need of rt.start()
    try:
        sleep(3) # runs the program x amount of times
    finally:
        rt.stop() # better in a try/finally block to make sure the program ends!

while True:
    input("Press enter to start the program\n")
    Timer_Start()