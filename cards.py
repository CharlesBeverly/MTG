import pandas as pd
def getCards(file): # takes in a json file from mtgjson.com and gets the rarity of the card and the srcyfallId, returns the all of those for a given set 

    df = pd.read_json(file)
    df = df.transpose()

    cardList = []

    for card in df["cards"]["data"]:
        cardList.append([card["rarity"],card["identifiers"]["scryfallId"]])
    
    return cardList