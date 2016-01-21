# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#next line imports the lxml.html library import lxml,html
#use the.fromstring function to turn html into a lxml 'object', a variable called 'root'
# # Read in a page
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
#tds = root.cssselect('td')
tds = root.cssselect('td')
record = {"cell" : td.text}
print record
scraperwiki.sqlite.save(["cell"], record)
#change 'td' to a different selector to scrape something else on the page
#lxml.html  - Parsing HTML (breaking it up and getting to a bit of it. lxml.html.fromstring 
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
