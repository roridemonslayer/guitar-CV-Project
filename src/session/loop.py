import time #this is being used for the countdown 
from src.shared.models import example_chord_chart, example_sound_verdict,example_vision_verdict
from src.session.scorer import is_chord_correct
for num in [3,2,1]:
    print (num)
    time.sleep(1)#pauses at the one second point doesn't move
print("Go!")

for entry in example_chord_chart["sequence"]:
    print(f"Play: {entry['chord']}")

    #here is our judgemebt scorer 
    result = is_chord_correct(entry['chord'],example_vision_verdict,example_sound_verdict, )
    print(f"Correct:{result}")



