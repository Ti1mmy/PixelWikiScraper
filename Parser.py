from bs4 import BeautifulSoup
import requests
with open("rawHTML.txt", "r", encoding="utf-8") as File1:
    file_contents = File1.read().split(sep="\n")
data = []
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'  # Get around rate limit
headers = {'User-Agent': user_agent}
skipped = []
for thing in file_contents:
    poke_id = thing.split('"')[1]
    poke_name = thing.split(">")[1]
    wiki_link = f'https://pixelmonmod.com{poke_id}'
    source = requests.get(wiki_link, headers=headers).text
    soup = BeautifulSoup(source, "lxml")
    for table in soup.find_all('span'):
        if "Ultra Rare" in table:
            data.append([wiki_link, poke_name, "Ultra Rare"])
            print(data[-1])
            break
        elif "Very Rare" in table:
            data.append([wiki_link, poke_name, "Very Rare"])
            print(data[-1])
            break
        elif "Rare" in table:
            data.append([wiki_link, poke_name, "Rare"])
            print(data[-1])
            break
        elif "Uncommon" in table:
            data.append([wiki_link, poke_name, "Uncommon"])
            print(data[-1])
            break
        elif "Common" in table:
            data.append([wiki_link, poke_name, "Common"])
            print(data[-1])
            break
    if poke_name not in data[-1]:
        print(f"Skipped {poke_name}")
        data.append([wiki_link, poke_name, "No Spawn/Legend"])
with open("wiki.txt", "a", encoding="utf-8") as output:
    for point in data:
        output.write(f'{point[0]}\n')
with open("name.txt", "a", encoding="utf-8") as output:
    for point in data:
        output.write(f'{point[1]}\n')
with open("chance.txt", "a", encoding="utf-8") as output:
    for point in data:
        output.write(f'{point[2]}\n')
