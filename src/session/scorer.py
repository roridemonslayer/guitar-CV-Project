from src.shared.models import example_vision_verdict, example_sound_verdict

def is_chord_correct(target_chord, vision_verdict, sound_verdict):
    vision_chord = vision_verdict["chord_shape"]
    sound_note = sound_verdict["sound_pick_up"]
    if vision_verdict['confidence'] < 0.7:
        return False
    return vision_chord == target_chord and sound_note == target_chord

print(is_chord_correct("F#", example_vision_verdict, example_sound_verdict))