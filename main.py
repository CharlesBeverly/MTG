import requests

# URL of the image
url = 'https://cards.scryfall.io/large/front/6/7/67f4c93b-080c-4196-b095-6a120a221988.jpg'
response = requests.get(url)

if response.status_code != 200:
    print("Failed to download image!")
    exit()


filename = "SecondCard.jpg" # You can name the file as you want
with open(filename, 'wb') as file:
    file.write(response.content)

print("Image downloaded successfully!")