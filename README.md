# wake
Wikipedia processing as easy as cAKE

# installation
```
pip install wake
```

# methods
### clean_title
takes in a title of a Wikipedia page as a string and escapes and cleans it of weird characters, so it can be put in a normal database

### download_if_necessary
dowloads a url to the system's temp directory if a file by its name isn't already there

### get_most_recent_available_dump
figures out what Wikipedia dump has certain subdumps complete

### tokenize
pass in the page text from a dump and get a list of tokens in return

### get_links
get links in an article(i.e. what's between '[[' and ']]')

### run_sql
runs MySQL command using bash with no external, third-party connector library required
```
from wake import run_sql

run_sql("SHOW DATABASES")

run_sql("SELECT COUNT(*) FROM geo_tags", "geo_tags_db")
```

# test
```
python3 -m unittest wake.test
```
