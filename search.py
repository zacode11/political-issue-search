import json
import re
import sys
import metapy
import pytoml
import os
import shutil

def create_dataset_folder():
    if not os.path.isdir("politiciandataset"):
        os.mkdir("politiciandataset")
    with open("politiciandataset/line.toml", "w+") as f:
        f.write("type = \"line-corpus\"")




def create_dat(filename):
    create_dataset_folder()
    issue_array = []
    with open(filename) as f:
        poli_json = json.load(f)
    with open("politiciandataset/politiciandataset.dat", "w+") as dat:
        for politician in poli_json:
            name = politician.get("name", "")
            image = politician.get("pic_url", "")
            issues = politician.get("issues", [])
            office = politician.get("office", "")
            for issue in issues:
                issue_name = issue.get("issue", 0)
                stances = issue.get("stances", [])
                for stance in stances:
                    list_item = {}
                    list_item["name"] = name
                    list_item["image"] = image
                    list_item["topic"] = re.sub('[\n\r]', '', issue_name)
                    list_item["document"] = re.sub('[\n\r]', '', stance)
                    dat_string = re.sub('[\n\r]', ' ', office) + "" + re.sub('[\n\r]', ' ', issue_name) + " " + re.sub('[\n\r]', ' ', stance)
                    for char in dat_string:
                        if(ord(char) > 128):
                            dat_string = dat_string.replace(char, '')
                    if(len(dat_string) < 3):
                        continue
                    dat.write(dat_string.lower())
                    dat.write("\n")
                    issue_array.append(list_item)
    with open("politiciandataset/formatted_politician_data.json", "w+") as f:
        json.dump(issue_array, f)

"""takes in q query, and returns a list of results from the dataset using metapy"""
def performSearch(q, number_of_results):
    if(os.path.isdir("idx")):
        shutil.rmtree("idx")
    idx = metapy.index.make_inverted_index('config.toml')
    query = metapy.index.Document()
    ranker = metapy.index.OkapiBM25(k1=1.2,b=0.75,k3=500)
    query.content(q.strip().lower())
    results = ranker.score(idx, query, number_of_results)
    return results

"""function used to display the results from the query. takes in the list of all issues and the results of the query. Creates a nicely formatted display of the results"""
def displayresults(issues, results):
    retval = []
    if(len(results) == 0):
        print("No Results Found")
        return
    displayable_results = {}
    list_of_topics = []
    for item in results:
        stance = issues[item[0]]
        if stance["topic"] not in displayable_results:
            displayable_results[stance["topic"]] = []
            list_of_topics.append(stance["topic"])
            displayable_results[stance["topic"]].append(stance["document"])
        else:
            displayable_results[stance["topic"]].append(stance["document"])
    for topic in list_of_topics:
        print("\n\n" + topic + ":")
        for position in displayable_results[topic]:
            print("\t" + position)
            retval.append(topic + ": " + position)
    return retval 


"""function used to create the json from the crawler and creates the dataset"""
def create_dataset():
    #include code here to generate pol.json file
    create_dat("pol.json")







"""function that performs and displays the search"""
def search(query, number_of_results):
    if not os.path.isdir("politiciandataset"):
	print("Creating dataset")
        create_dataset()
    print("Searching for \"" + query + "\"")
    with open("politiciandataset/formatted_politician_data.json") as f:
        list_of_issues = json.load(f)
    result_indices = performSearch(query, number_of_results)
    result_array = displayresults(list_of_issues, result_indices)


"""the first argument given to the script will be used as the
    Second argument is the number returned results
    Example: python search.py "Dick Durbin" 3
"""
def main():
    num_results = 10
    query = ""
    if(len(sys.argv) == 1):
        print("Please provide a query. And call this script in the form: python search.py [query]")
        print("Optionally, can provide a second argument for the number of desired results: python search.py [query] [num_results]")
        return
    if(len(sys.argv) > 1):
        query = sys.argv[1]
    if(len(sys.argv) > 2):
        try:
            num_results = int(sys.argv[2])
        except ValueError:
            print("Second argument must be a number (number of desired results)")
            return
    search(query, num_results)

main()
