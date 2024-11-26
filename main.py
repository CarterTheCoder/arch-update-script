# This script will update Arch Linux based systems
# and use the notify-send command to notify the
# user of the success or failure of the update.


import os

def notify(text):
    os.system(f"notify-send --app-name=Update-Scripts '{text}'")

def update_system():
    return_code = os.system("yes | sudo pacman -Syu")
    if return_code == 0:
        notify("Update was successful.")
    else:
        notify(f"Update was not successful. Return Code: {return_code}")

def main():
    update_system()

if __name__ == "__main__":
    main()
