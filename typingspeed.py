import time

sentence = "Python is a powerful programming language"
print("Type this:\n", sentence)

start = time.time()
typed = input()

end = time.time()

time_taken = end - start
speed = len(typed.split()) / (time_taken / 60)

print("Time:", round(time_taken,2), "sec")
print("Speed:", round(speed,2), "WPM")
