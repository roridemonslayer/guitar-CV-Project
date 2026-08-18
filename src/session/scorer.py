from src.shared.models import example_vision_verdict, example_sound_verdict

def is_chord_correct(target_chord, vision_verdict, sound_verdict):
    vision_chord = vision_verdict["chord_shape"]
    if vision_verdict['confidence'] < 0.7:
        return False
    if sound_verdict['volume'] < 0.005:
        return False
    return vision_chord == target_chord

if __name__ == "__main__":
    print(is_chord_correct("G", example_vision_verdict, example_sound_verdict))