# Motivation

There is a very low amount SpreadSheet (Excel, Numbers, etc) type datasets
readily available for consumption for data science applications. My hypothesis
is that the internet will have similar format of data (rows, columns, w/ numeric
relations between the cells) in the table tag of html data from the web. And
with the sheer volume of html data we can extract a very large dataset from these
websites.

# Purpose

The table-collector library allows you to collect html data from info inside
table tags on the public web. It fires off a spider which crawls the web
and looks for these tags. It uses a heuristic that a certain percentage of the
table td tags should have solely numeric values so that we don't get tables
that are only labeled tables for style purposes. The data writes to a text file
as it is crawling

# Installation

Probably want to make a virtualenv first, then

```
$ pip install -r requirements.txt
```

# Run

```
$ scrapy runspider spider.py
```

or

```
$ scrapy runspider --nolog spider.py
```

## TXT File Format
The output text file will have each html table tag entry separated by a single
new line char.

