import time #this is being used for the countdown 
from src.shared.models import example_chord_chart
for num in [3,2,1]:
    print (num)
    time.sleep(1)#pauses at the one second point doesn't move
print("Go!")

for entry in example_chord_chart["sequence"]:
    print(f"Play: {entry['chord']}")