from gtts import gTTS
import playsound
tts = gTTS(text='สวัสดียินดีที่ได้รู้จักค่ะ', lang='th')
tts.save("sound.mp3")
playsound.playsound("sound.mp3", True)