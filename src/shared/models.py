# this file handle Shared data shapes ("contracts") that packages use to talk to each other.

example_vision_verdict = {
    "chord_shape": "G", #the chord it thinks im making 
    "confidence" : 0.87, # how sure it is that im making this chord 
    "timestamp" : 12.43, # how many seconds into it the song it's been
}

example_sound_verdict ={
    "sound_pick_up" :"F#", #the sound it picked up was this
    "confidence" : 0.87,   #how confident it's this sound
    "timestamp": 13.45, 
    "volume" : 20.67, 
}