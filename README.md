# EC 500 Project - News Analyzer

News Analyzer is an evolving web-based application that uses various APIs to allow users to upload documents, search newsfeeds, and analyze text.

## Setup

- Clone and `cd` into repository
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip3 install -r requirements.txt`
- `cd` into the module that you would like to test and run with `python3 [filename]`

## User Stories

**End User**

- As a journalist, I want to upload important documents to the cloud to parse the text for analysis.
- As a journalist, I want to be able to see what articles are relevant to the topics that I want to research.
- As a journalist, I want to analyze text with or without a document to see what is the overall sentiment of the text.

**Developer**

- As a developer, I want to be able to call indiviual endpoints of various APIs to extract the data I need for my own app.
- As a developer, I want to manage a local or cloud-based database with relational tables to see who has upload what information.
- As a developer, I want to manage a login in systme so only authorized users can access the news analyzer.

## Current Modules

[News Analyzer](https://github.com/BUEC500C1/news-analyzer-benleone90/tree/master/news)
[Natural Language Processing](https://github.com/BUEC500C1/news-analyzer-benleone90/tree/master/nlp)
[PDF File Uploader](https://github.com/BUEC500C1/news-analyzer-benleone90/tree/master/upload)
[User Login](https://github.com/BUEC500C1/news-analyzer-benleone90/tree/master/login)

## Reference/Resources

- Many resources and other APIs were found from this [public-apis repo](https://github.com/public-apis/public-apis).
- The news injester API uses [NewsAPI.org](https://newsapi.org/) to create custom endpoints.
