import requests
import os
from colors import *

def getCard():
    os.system("cls" if os.name == 'nt' else 'clear')
    str = input(f"{CWHITE}ENTER A CARD NAME TO SEARCH:\n{CYELLOW2}>")

    response = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={str}")
    if response.status_code == 200:
        card = response.json()

        # print out the details of the searched for card ->
        print(f"""
{CWHITEBG}{CBLACK}Card Name:\n{CEND}{CGREEN}{card["name"]}\n\n
{CWHITEBG}{CBLACK}Oracle Text:\n{CEND}{CGREEN}{card["oracle_text"]}\n\n
{CWHITEBG}{CBLACK}Mana Cost:\n{CEND}{CGREEN}{card["mana_cost"]}\n\n
{CWHITEBG}{CBLACK}Type:\n{CEND}{CGREEN}{card["type_line"]}\n\n
{CWHITEBG}{CBLACK}Price:\n{CEND}{CGREEN}${card["prices"]['usd']}\n
        {CEND}""")

        repeat = input(f"{CWHITE}ENTER 'Y' TO SEARCH FOR A NEW CARD, OR 'N' TO EXIT.\n")
        if repeat == 'y':
            os.system("cls" if os.name == 'nt' else 'clear')
            getCard()
        return
    else:
        print(f"{CREDBG}{CWHITE}NO CARD WITH THE GIVEN NAME FOUND, OR TOO VAGUE OF A SEARCH.{CEND}")
        repeat = input("ENTER 'Y' TO SEARCH FOR A NEW CARD, OR 'N' TO EXIT.\n")
        if repeat.lower() == 'y':
            os.system("cls" if os.name == 'nt' else 'clear')
            getCard()
        return

def getCardByOracleText():
    query = input(f"{CWHITE}ENTER ORACLE TEXT TO LOOK UP CARDS BY:{CYELLOW2}\n> ")
    response = requests.get(f"https://api.scryfall.com/cards/search?q=oracle_text={query}")

    print(response.json())

getCard()
# getCardByOracleText()
