# Politician Stance Search Engine
Our search engine is geared towards people who are interested in politics and want to view the stances of politicians on various issues, such as education, healthcare, and economic policy. This search engine can also help independent and undecided voters determine which candidates align with their stances and opinions.

This project provides a python API, a web application, and a command line interface.

Candidates can be found for Congressional elections, statewide elections (gubernatorial and senate), and presidential.
You can type in anything related to politics and elections and it will show up. Here are some examples for search suggestions:
1. "Illinois education"
2. "Bernie Sanders"
3. "Rand Paul Healthcare"
4. "Peter Roskam"

The search engine will return relevant results on politician stances.

[Link to video explaining our search engine](https://mediaspace.illinois.edu/media/t/1_ibg1bhzy)

## Getting Started
To access and run the code for this project, [Download](https://github.com/zacode11/political-issue-search/archive/master.zip) or Clone the entire repository using `git clone https://github.com/zacode11/political-issue-search.git`

### Prerequisites
#### To Use the Crawler if the Dataset, the  [Politiciandataset](https://github.com/zacode11/political-issue-search/blob/master/politiciandataset) Folder, is not Downloaded/In the Directory
The crawler is built with scrapy. Use the following command to download the scrapy python package.
```bash
pip install scrapy
```
Within the main directory containing scrapy.cfg, run the following command to scrape the data (if you want to scrape it again)
```bash
scrapy crawl oti -o pol.json
```
This will generate a list of json objects in [pol.json](https://github.com/zacode11/political-issue-search/blob/master/pol.json)
#### Other Prerequisites
This project uses [metapy](https://github.com/meta-toolkit/metapy) Use the following steps to download.
```bash
pip install metapy pytoml
```
If you are on an EWS machine:
```bash
module load python3
# install metapy on your local directory
pip install metapy pytoml --user
```
This project also uses *JSON* and *Regular Expression (RegEx)*. Both are part of the python core library and will function as long as Python 2.6 or greater is being used.

The Django web app requires the Django package that can be installed as follows.
```bash
pip install django==2.05
```

### Setting Up the Environment
As long as the user has downloaded all the necessary files and installed all the prerequisite libraries, the environment should be all set up.

#### config.toml
Note: To rank the relevance of different documents for a given query, this project uses BM25 with the unigram analyzer. If the user wishes to use a different analyzer, such as a bigram for example, they can do so by editing the [config.toml](https://github.com/zacode11/political-issue-search/blob/master/config.toml) file. The following section can be altered to make such a change.
```toml
[[analyzers]]
method = "ngram-word"
ngram = 1
filter = "default-unigram-chain"
```

## Command Line Interface
The searching functionality can be executed on the terminal with the following command. The results of the search will be printed to the terminal
```bash
# basic structure
python search.py query

# example
python search.py "Jeff Sessions on abortions"
```
An optional argument can be passed in to specify the number of desired results to be displayed. The default is 10 if no argument is passed in.
```bash
# basic structure
python search.py query number_of_results

#example
#Note that the default number of results is 10
python search.py "Jeff Sessions on abortions" 3
```

Running the code on the terminal will generate the dataset, the [politiciandataset](https://github.com/zacode11/political-issue-search/blob/master/politiciandataset) folder as well as create an inverted index if either of them do not already exists in the project. This may result in the first execution taking significantly longer than subsequent runs. In the case the [politiciandataset](https://github.com/zacode11/political-issue-search/blob/master/politiciandataset) folder needs to be created, if [pol.json](https://github.com/zacode11/political-issue-search/blob/master/pol.json) is not in the current directory, it will be created as well using the scrapy crawler.       



## Python API
Include the following line at the top of the python script:
```python
# to gain access to the search methods
import search
```
This will give the user access to the methods in [search.py](https://github.com/zacode11/political-issue-search/blob/master/search.py)
The important methods are as follows:
#### create_dataset()
This method will create the [politiciandataset](https://github.com/zacode11/political-issue-search/blob/master/politiciandataset) folder for use by the search engine. This method will overwrite the folder if it already exists. Additionally, this method will create the [pol.json](https://github.com/zacode11/political-issue-search/blob/master/pol.json) file using the scrapy crawler if it does not exist in the current directory (make take up to 30 seconds).
```python
# example call
search.create_dataset()
```

#### clear_dataset()
This method will clear the existing dataset files/folders. It will delete the following files/folders if they exist: [politiciandataset](https://github.com/zacode11/political-issue-search/blob/master/politiciandataset), [idx](https://github.com/zacode11/political-issue-search/blob/master/idx), and [pol.json](https://github.com/zacode11/political-issue-search/blob/master/pol.json)
```python
#example call
search.clear_dataset()
```


#### search(query, number_of_results, print_results = True)
This method takes in 3 parameters, the query, the number of desired results, and whether to print the results to the terminal. The third parameter, print_results is set to True by default, so it may be omitted if the user wishes for the results to be printed. This method will perform the search using the BM25 algorithm. It will print the results to the terminal, as well as provide a list of strings, where each string is a relevant document. The documents in the list are in descending order according to relevance. The first call of this function may take additional time to run if the inverted index, *idx*, folder has not been created yet.

```python
# example code where print_results is omitted
result_array = search.search("Richard Durbin on Education", 20)
# will return a list of strings of size at most 20.
# The size will be less than 20 if there are not 20 relevant results.
# Each list entry will be formatted as follows: "Document_name: document_content"
# The results will be printed to the terminal

# example code where results will not be printed
result_array = search.search("Richard Durbin on Education", 20, False)
```
Note: This method will call the **create_dataset()** if the [politiciandataset](https://github.com/zacode11/political-issue-search/blob/master/politiciandataset) folder is not in the same directory.

## Django Web App

Finally, we included a web app to show off a simple use case of the Python API.

To run the webapp, make sure you have both the root directory of the repo and the webapp directory downloaded locally. Withing the webapp directory run the following command to run the webserver.
```bash
python manage.py runserver
```
If you open a web browser and access *http://127.0.0.1:8000* you will find the web app where you can search for some politician and/or political phrases and recieve a results page with some cards showing resulting information. Users can return to the initial search page by clicking on the badge labelled Political Search.

## Contributions
Prithvi Ramanathan worked on and documented the python searching API and the command-line interface.
Zac Codiamat worked on and documented the scrapy web crawler to get the politician data and the web application.
AJay Jain came up with the idea and structure of the project, completed the project proposal and progress report, and worked on/edited the video tutorial.
