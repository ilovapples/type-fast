# from getkey import getkey
from pytermgui import tim, Window


MENU_TXT = """
  _________  __   __  ______    _______
  |__   __|  \ \ / /  | ___ \  |  _____|
     | |      \   /   | |_| |  | |____
     | |       \ /    | ____/  |  ____|
     | |       | |    | |      | |_____
     |_|       |_|    |_|      |_______|
  _________     __       _____  _______
  |  _____|    /  \     |  ___| |__   __|
  | |___      / /\ \    | |___     | |   
  |  ___|    / /__\ \   |___  |    | |   
  | |       /  /  \  \   ___| |    | |   
  |_|      /__/    \__\ |_____|    |_|
"""

def menu():
    """Opens menu
    """
    tim.print(f"[deepskyblue @black]{MENU_TXT}")
    tim.print("[deepskyblue @black]n")


def main():
    """Starts program
    """
    menu()
  

if __name__ == "__main__":
    main()
