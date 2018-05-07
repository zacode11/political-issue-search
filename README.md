# Politician Stance Search Engine
Insert Project Description Here

## Getting Started
There are several ways to access and run the code for this project.
1. [Download](https://github.com/zacode11/political-issue-search/archive/master.zip) or Clone the entire repository using `git clone https://github.com/zacode11/political-issue-search.git`
2. Alternatively, the searching functionalities will execute if only the [stopword.txt](https://github.com/zacode11/political-issue-search/blob/master/stopwords.txt), [search.py](https://github.com/zacode11/political-issue-search/blob/master/search.py), and [config.toml](https://github.com/zacode11/political-issue-search/blob/master/config.toml) files along with the [politiciandataset](https://github.com/zacode11/political-issue-search/blob/master/politiciandataset) folder are downloaded.
3. Lastly, if the user wishes to recreate the dataset using the crawler provided, instead of downloading the dataset provided, the following files will be necessary:

### Prerequisites
#### To Use the Crawler If the Dataset is Not Downloaded
Insert Description on how to use the crawler
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
This project also uses *JSON* and *Regular Expression (RegEx)*. So, these will also need to be installed/downloaded. Both are part of the python core library and will function as long as Python 2.6 or greater is being used. 

### Installation
Insert installation instructions here

## Running Script on the Terminal
The searching functionality can be executed on the terminal with the following command. The results of the search will be printed to the terminal
```bash
# basic structure
python search.py query

# example
python search.py "Jeff Session on abortions"
```
An optional argument can be passed in to specify the number of desired results to be displayed. The default is 10 if no argument is passed in.
```bash
# basic structure
python search.py query number_of_results

#example
python search.py "Jeff Sessions on abortions" 3
```

Running the code on the terminal will generate the dataset, the [politiciandataset](https://github.com/zacode11/political-issue-search/blob/master/politiciandataset) folder, as well as create an inverted index if neither already exists in the project. This may result in the first execution taking significantly longer than subsequent runs.



## Executing Specific Methods from Another Script
Include the following line at the top of the python script:
```python
# to gain access to the search methods
from search import *
```
This will give the user access to the methods in [search.py](https://github.com/zacode11/political-issue-search/blob/master/search.py)
The important methods are as follows:
#### create_dataset()
This method will create the *politiciandataset* folder for use by the search engine.
```python
# example call
create_dataset()
```

#### search(query, number_of_results)
This method takes in 2 parameters, the query as well as the number of desired results. This method will perform the search using the BM25 algorithm. It will print the results to the terminal, as well as provide a list of strings, where each string is a relevant document. The documents in the list are in decending order according to relevance. The first call of this function may take additional time to run if the inverted index, *idx*, folder has not been created yet.
```python
# example code
result_array = search("Richard Durbin on Education", 20)
# will return an list of strings of size at most 20.
# The size will be less than 20 if there are not 20 relevant results. 
# Each list entry will be formatted as follows: "Document_name: document_content"
```

