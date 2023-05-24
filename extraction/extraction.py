from kiwipiepy import Kiwi
import os

kiwi = Kiwi()

for file in os.listdir("../crawling/location_keyword"):
    total = []
    file_list = file.split("_")
    city_name = file_list[0].strip()

    ff = open(city_name + "_extraction.txt", 'w', encoding='UTF-8')

    with open(os.path.join("../crawling/location_keyword", file), "r") as f:
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))
        for line in lines:
            results = []
            result = kiwi.analyze(line)
            for token, pos, _, _ in result[0][0]:
                if len(token) != 1 and pos.startswith('N') or pos.startswith('SL'):
                    ff.write(token + "\n")
    ff.close()

f.close()
