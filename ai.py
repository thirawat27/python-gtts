from gtts import gTTS
import playsound
tts = gTTS(text='สวัสดีค่ะ,ยินดีที่ได้รู้จักค่ะ,ฉันชื่อสมศรีค่ะ', lang='th')
tts.save("sound.mp3")
playsound.playsound("sound.mp3", True)