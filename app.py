from pygame import mixer

# Instantiate mixer
mixer.init()

mixer.music.load('sound2.mp3')
sound = mixer.Sound('sound2.mp3')

print("Music playing")
mixer.music.set_volume(1)
mixer.music.play()
print(f"length: {sound.get_length()/60}")

while True:
    x = input("Text: ")
    if x == 'e':
        mixer.music.pause()
        print(mixer.music.get_pos()/60)
    if x == 'p':
        mixer.music.unpause()
        print(mixer.music.get_pos()/60)
