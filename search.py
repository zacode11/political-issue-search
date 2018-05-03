import json
import re


def create_dat(filename):
    issue_array = []
    with open(filename) as f:
        poli_json = json.load(f)
    with open("politiciandataset/politiciandataset.dat", "w+") as dat:
        for politician in poli_json:
            name = politician.get("name", "")
            image = politician.get("pic_url", "")
            issues = politician.get("issues", [])
            for issue in issues:
                issue_name = issue.get("issue", 0)
                stances = issue.get("stances", [])
                for stance in stances:
                    list_item = {}
                    list_item["name"] = name
                    list_item["image"] = image
                    list_item["topic"] = issue_name
                    list_item["document"] = stance
                    dat_string = re.sub('[\n\r]', ' ', issue_name) + " " + re.sub('[\n\r]', ' ', stance)
                    for char in dat_string:
                        if(ord(char) > 128):
                            dat_string = dat_string.replace(char, '')
                    if(len(dat_string) < 3):
                        continue
                    dat.write(dat_string)
                    dat.write("\n")
                    issue_array.append(list_item)

def main():
    create_dat("pol.json")
main()
