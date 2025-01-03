# import time
# for  i in range(1,11):
#     print(f"\rProcessing: {i}%", end="clear")
#     time.sleep(.5)

# print("\nDone")  

import time

for i in range(101):
    # print(f"Progress: [{i}%]",end=" ",flush=True)
    # print(f"Progress: [{i}%]",end=" ")
    # print(f"Progress: [{i}%]",end=" ")
    # print(f"\rProgress: [{i}%]",end=" ")
    print(f"\rProgress: [{i}%]",end=" ",flush=True)
    time.sleep(0.01)  # Simulating work
