from bs4 import BeautifulSoup
import pyautogui
import pyperclip  # for foreign languages and uncommon characters
import re
import requests
import time

# GLOBAL VARIABLES
MSG_DELAY = 5  # in seconds


def main():
    web_URL = get_user_input()
    # waiting for user to switch tabs
    time.sleep(5)
    lyrics = get_lyrics(web_URL)
    print_lyrics(lyrics)


def get_user_input():
    pattern = "^(https://www\.azlyrics\.com)(\.az)?[a-zA-Z0-9#\./-]"
    user_input = input("Give me a song: ")
    while not re.search(pattern, user_input):  # re-prompting user if URL provided is invalid
        user_input = input("USAGE: Paste song URL link from azlyrics.com.az: ")
    print("SUCCESS! You have 5 seconds to enter a chat window and place your cursor in the chat input box.")
    return user_input


def get_lyrics(web_URL):
    page = requests.get(web_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        match = soup.find('div', class_="col-xs-12 col-lg-8 text-center").text
    except Exception as e:
        match = "Invalid URL"
    all_text = match.split("\n")  # casting string to array
    lyrics = []
    for line in all_text:  # removing empty and irrelevant elements
        if line == ' Submit Corrections':
            break
        if line != '' and line != ' ' and line != '  ':
            lyrics.append(line)
    return lyrics


def print_lyrics(lyrics):
    while True:
        for line in lyrics:
            pyperclip.copy(line)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press("enter", interval=MSG_DELAY)
        pyautogui.typewrite("STAN JIHYO, TZUYU, NAYEON, SANA, MOMO, DAHYUN, MINA, JEONGYEON & CHAEYOUNG")
        pyautogui.press("enter")
    return


if __name__ == "__main__":
    main()
