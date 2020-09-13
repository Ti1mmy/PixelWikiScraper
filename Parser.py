from bs4 import BeautifulSoup
import requests
with open("rawHTML.txt", "r", encoding="utf-8") as File1:
    file_contents = File1.read().split(sep="\n")
data = []
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'  # Get around rate limit
headers = {'User-Agent': user_agent}
skipped = []
types = []
for thing in file_contents:
    poke_id = thing.split('"')[1]
    poke_name = thing.split(">")[1]
    wiki_link = f'https://pixelmonmod.com{poke_id}'
    source = requests.get(wiki_link, headers=headers).text
    soup = BeautifulSoup(source, "lxml")
    for table in soup.find_all('span'):
        if "Ultra Rare" in table:
            data.append([wiki_link, poke_name, "Ultra Rare"])
            break
        elif "Very Rare" in table:
            data.append([wiki_link, poke_name, "Very Rare"])
            break
        elif "Rare" in table:
            data.append([wiki_link, poke_name, "Rare"])
            break
        elif "Uncommon" in table:
            data.append([wiki_link, poke_name, "Uncommon"])
            break
        elif "Common" in table:
            data.append([wiki_link, poke_name, "Common"])
            break
    if poke_name not in data[-1]:
        print(f"{poke_name} does not naturally spawn")
        data.append([wiki_link, poke_name, "No Spawn/Legend"])
    typeName = []
    for type in soup.find_all('a'):
        if '<span style="color:#FFFFFF;">' in str(type):
            typeName.append(str(type).split('"')[3])
    formatted_type = []
    for individual_type in typeName:
        if individual_type not in formatted_type:
            if individual_type == 'Psychic (type)':
                formatted_type.append('Psychic')
            else:
                formatted_type.append(individual_type)
    data[-1].append(formatted_type)
    print(data[-1])

with open("wiki.txt", "a", encoding="utf-8") as output:
    for point in data:
        output.write(f'{point[0]}\n')
with open("name.txt", "a", encoding="utf-8") as output:
    for point in data:
        output.write(f'{point[1]}\n')
with open("chance.txt", "a", encoding="utf-8") as output:
    for point in data:
        output.write(f'{point[2]}\n')
with open("types.txt", "a", encoding='utf-8') as output:
    for point in data:
        output.write(f'{"/".join(point[3])}\n')
