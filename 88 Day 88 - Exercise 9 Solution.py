# For Windows using win32com.client
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
names = ["rohan", "joe", "jane", "tom"]
for name in names:
    speak.Speak(f'Shoutout to {name}')


# For Mac
from os import system
names = ["rohan", "joe", "jane", "tom"]
for name in names:
  system(f'say Shoutout to {name}')