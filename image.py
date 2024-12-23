import requests
def getImage(scryfallid, loc): # gets the image associated to the scryfall id, and saves it to the folder provied in loc 
    # URL of the image
    url = 'https://cards.scryfall.io/large/front/'+ scryfallid[0] +'/'+ scryfallid[1] +'/'+ scryfallid +'.jpg'
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to download image!")
        exit()


    filename = loc + scryfallid + ".png" # You can name the file as you want
    with open(filename, 'wb') as file:
        file.write(response.content)
