import subprocess
import re
import pyperclip
import time
import pyautogui  # For automating the paste action

def get_latest_sms():
    # Your code for getting the latest SMS
    # ...

def extract_code_from_sms(sms):
    # Your code for extracting OTP
    # ...

def copy_to_clipboard(text):
    pyperclip.copy(text)
    print(f"Copied to clipboard: {text}")

def paste_code():
    time.sleep(1)  # Pause briefly to ensure the right window is active
    pyautogui.hotkey('ctrl', 'v')  # Simulate Ctrl+V (paste)
    print("Code pasted successfully!")

def main():
    # Your main function code
    # ...

if __name__ == "__main__":
    main()
