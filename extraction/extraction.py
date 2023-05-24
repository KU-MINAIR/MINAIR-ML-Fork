from kiwipiepy import Kiwi
import os, re

kiwi = Kiwi()

for file in os.listdir("../crawling/location_keyword"):
    total = []
    file_list = file.split("_")
    city_name = file_list[0].strip()

    if city_name == ".DS":
        continue

    ff = open("../extraction/extraction_keyword/" + city_name + "_extraction.txt", 'w', encoding='UTF-8')
    with open(os.path.join("../crawling/location_keyword", file), "r") as f:
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))
        for line in lines:
            kor_str = re.sub(r"[^가-힣\s]", "", line) # 한글만 추출
            result = kiwi.analyze(kor_str)
            for token, pos, _, _ in result[0][0]:
                if len(token) != 1 and pos.startswith('N'):
                    ff.write(token + "\n")
    ff.close()

f.close()
