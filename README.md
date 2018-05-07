# Politician Stance Search Engine
Insert Project Description Here

## Getting Started
There are several ways to access and run the code for this project.
1. Download or Clone the entire repository using `git clone https://github.com/zacode11/political-issue-search.git`
2. Alternatively, the searching functionalities will execute if only the [stopword.txt](https://github.com/zacode11/political-issue-search/blob/master/stopwords.txt), [search.py](https://github.com/zacode11/political-issue-search/blob/master/search.py), and [config.toml](https://github.com/zacode11/political-issue-search/blob/master/config.toml) files along with the [politiciandataset](https://github.com/zacode11/political-issue-search/blob/master/politiciandataset) folder are downloaded.
3. Lastly, if the user wishes to recreate the dataset using the crawler provided, instead of downloading the dataset provided, the following files will be necessary:

### Prerequisites
#### To Use the Crawler if the Dataset is not Downloaded
#### Other Prerequisites
This project uses [metapy](https://github.com/meta-toolkit/metapy) Use the following steps to download.
`pip install metapy pytoml`
If you are on an EWS machine:
```bash
module load python3
# install metapy on your local directory
pip install metapy pytoml --user
```
### Installation
Insert installation instructions here

## Running Script on the Terminal
The searching functionality can be executed on the terminal with the following command.
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

