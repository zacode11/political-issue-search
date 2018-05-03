import json
import re
import sys
import metapy
import pytoml

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
                    list_item["topic"] = re.sub('[\n\r]', '', issue_name)
                    list_item["document"] = re.sub('[\n\r]', '', stance)
                    dat_string = re.sub('[\n\r]', ' ', issue_name) + " " + re.sub('[\n\r]', ' ', stance)
                    for char in dat_string:
                        if(ord(char) > 128):
                            dat_string = dat_string.replace(char, '')
                    if(len(dat_string) < 3):
                        continue
                    dat.write(dat_string.lower())
                    dat.write("\n")
                    issue_array.append(list_item)
    return issue_array

"""takes in q query, and returns a list of results from the dataset using metapy"""
def performSearch(q):
    idx = metapy.index.make_inverted_index('config.toml')
    query = metapy.index.Document()
    ranker = metapy.index.OkapiBM25(k1=1.2,b=0.75,k3=500)
    num_results = 10
    query.content(q.strip().lower())
    results = ranker.score(idx, query, num_results)
    return results

"""function used to display the results from the query. takes in the list of all issues and the results of the query. Creates a nicely formatted display of the results"""
def displayresults(issues, results):
    displayable_results = {}
    for item in results:
        stance = issues[item[0]]
        if stance["topic"] not in displayable_results:
            displayable_results[stance["topic"]] = []
            displayable_results[stance["topic"]].append(stance["document"])
        else:
            displayable_results[stance["topic"]].append(stance["document"])
    for topic in displayable_results:
        print("\n\n" + topic + ":")
        for position in displayable_results[topic]:
            print(position)



def main():
    list_of_issues = create_dat("pol.json")
    query = ""
    if(len(sys.argv) > 1):
        query = sys.argv[1]

    results = performSearch(query)
    displayresults(list_of_issues, results)
main()
