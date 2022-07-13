import requests
import os

def getCard():
    os.system("cls" if os.name == 'nt' else 'clear')
    str = input("\nType in a card name:\n")

    response = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={str}")
    if response.status_code == 200:
        card = response.json()

        # print out the details of the searched for card ->
        print(f"""
    Card Name:\n    {card["name"]}\n\n
    Oracle Text:\n  {card["oracle_text"]}\n\n
    Mana Cost:\n    {card["mana_cost"]}\n\n
    Type:\n     {card["type_line"]}\n\n
        """)

        repeat = input("Enter 'y' to look for another card, or 'n' to exit.\n")
        if repeat == 'y':
            os.system("cls" if os.name == 'nt' else 'clear')
            getCard()
        return
    else:
        print("No card with that name found")
        getCard()

getCard()
