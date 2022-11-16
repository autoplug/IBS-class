# pip install schedule
# https://schedule.readthedocs.io/en/stable/examples.html#run-a-job-every-x-minute
import schedule


def say_hello():
    print("Hello World!...")

def say_hello2():
    print("Hola")


schedule.every(1).seconds.do(say_hello)
schedule.every(2).seconds.do(say_hello2)

while True:
    schedule.run_pending()


