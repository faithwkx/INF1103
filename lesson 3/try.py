# #Iteration (Loop) Control: while
# walk_circle = 0
# while walk_circle < 10:
#     walk_circle += 1
# print("walking complete")
# print(walk_circle)

# # Iteration (Loop) Control: for 
# walk_circle = 0
# for walk_circle in range(10):
#     print(walk_circle)
# print("walking complete")
# print(walk_circle)

# # Break Statement
# walk_circle = 0
# for walk_circle in range(1,10):
#     print(walk_circle)
#     if walk_circle == 5:
#         break
# print("walking complete")
# print(walk_circle)

# # Continue Statement
# walk_circle = 0
# for walk_circle in range(1,10):
#     print(walk_circle)
#     if walk_circle == 5:
#         continue
# print("walking complete")
# print(walk_circle)

#Task for the day!!
import time
light = input("Enter the traffic light color (green, yellow, red): ").lower()

for seconds in range(10):
    if light == "green":
        print("Go!")
    elif light == "yellow":
        print("Slow down!")
    elif light == "red":
        print("Stop!")
    else:
        print("Invalid traffic light color!")
        break
    time.sleep(1)