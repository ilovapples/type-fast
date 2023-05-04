from termcolor import colored
from getkey import getkey, keys
import time
import platform
from wonderwords import RandomWord

randomWords = RandomWord()

wpm = []

try:
    import replit
    def clear():
        clear()
except:
    import os
    if platform.system() == 'Windows':
        def clear():
            os.system('cls')
    else:
        def clear():
            os.system('clear')


class Format:
    end = '\033[0m'
    underline = '\033[4m'
    bold = '\033[1m'


def ul(string):
    """Return an underlined version of the specified string."""
    return Format.underline + string + Format.end


def bld(string):
    """Return a bold version of the specified string."""
    return Format.bold + string + Format.end


def showStats(typingTime, wordcnt):
    clear()
    grossWPM = wordcnt / (typingTime / 60)
    wpm.append(float(str(grossWPM)[:str(grossWPM).index('.') + 4]))
    clear()
    print("——" + colored(bld(" STATS "), 'blue') + "——\n")
    print(
        colored("Gross WPM: ", 'blue') +
        colored(("%.3f" % grossWPM), 'light_yellow'))

    print("\n" + colored("Press the space key to continue...", 'grey'))
    key = ""
    while True:
        key = getkey()
        if key == " ":
            clear()
            title()


def avrge(list):
    total = 0
    for i in list:
        total += i
    return total / len(list)


def test(words, wordCount):
    clear()
    selectedChar = 0
    print(colored(ul(words[0]), 'blue') + words[1:])
    startTime = time.time()
    typedKeys = ""
    key = ""
    while True:
        listOF_FINAL = []
        typedKeys = [char for char in words[:selectedChar]]
        key = getkey()
        if key == words[selectedChar]:
            selectedChar += 1
            try:
                typedKeys += words[selectedChar]
            except IndexError:
                break
        elif key == "\x1b":
            testTitle()
        for i, letter in enumerate(words):
            if i == selectedChar:
                listOF_FINAL.append(colored(ul(letter), 'blue'))
            else:
                listOF_FINAL.append(letter)

        index = 0
        for _ in range(selectedChar):
            listOF_FINAL[index] = colored(listOF_FINAL[index], 'dark_grey')
            index += 1

        stringOFFINAL = ""
        for i in listOF_FINAL:
            stringOFFINAL += i

        clear()
        print(stringOFFINAL)

    endTime = time.time()

    showStats(endTime - startTime, wordCount)


def startTest(wordcnt):
    """Start the typing test."""
    clear()
    words = ""
    clear()
    for i in range(wordcnt):
        words += randomWords.word() + " "
        clear()

    words = words.strip()
    # Start countdown.
    for i in range(3, 0, -1):
        clear()
        print(
            colored("Starting in ", 'blue') + colored(i, 'yellow') +
            colored("...", 'blue'))
        print(colored(words, 'dark_grey'))
        time.sleep(1)

    # Start test.
    test(words, wordcnt)


def statsTitle():
    clear()
    print("——" + colored(bld(" YOUR STATS "), 'blue') + "——\n")
    if len(wpm) > 0:
        print(
            colored("Average Gross WPM: ", 'blue') +
            colored(("%.3f" % avrge(wpm)), 'yellow'))
        print(
            colored("Highest Gross WPM: ", 'blue') +
            colored(max(wpm), 'yellow'))
    else:
        print(
            colored(
                "\nYou haven't taken a test yet! (at least, not on this run...)",
                'green'))

    print(colored("Press the space key to continue...", 'grey'))
    key = ""
    while True:
        key = getkey()
        if key == " ":
            title()
            break


def testTitle():
    clear()
    print(colored(bld("TYPING TEST") + '\n', 'blue'))
    print(
        "How many words do you want to type\nfor the test? (input integer or input 'back' to go back)"
    )
    wordCount = input(colored("Word count: ", 'blue')).lower()
    if wordCount == 'back':
        title()
    try:
        if int(wordCount) < 1:
            testTitle()
        startTest(int(wordCount))
    except:
        testTitle()


def title_SELECTtest():
    clear()
    print(colored(bld("MAIN TITLE\n"), 'blue'))
    print(colored("Test", 'light_blue') + " <")
    print(colored("Stats", 'light_blue'))
    key = ""
    while True:
        key = getkey()
        if key == "\n":
            testTitle()
        if key == keys.DOWN or key == keys.UP:
            title_SELECTstat()


def title_SELECTstat():
    clear()
    print(colored(bld("MAIN TITLE\n"), 'blue'))
    print(colored("Test", 'light_blue'))
    print(colored("Stats", 'light_blue') + " <")
    key = ""
    while True:
        key = getkey()
        if key == "\n":
            statsTitle()
        if key == keys.UP or key == keys.DOWN:
            title_SELECTtest()


def title():
    title_SELECTtest()


title_SELECTtest()
