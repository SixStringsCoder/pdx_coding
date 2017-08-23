import bs4, requests, re

# get webpage contact
response2 = requests.get('https://store.pariyatti.org/eBooks_ep_49-1.html')

# check for 200 success
response2.raise_for_status

# pass text attribute of the response
soup_results = bs4.BeautifulSoup(response2.text)

# store just class with author names on webpage in variable
authors = soup_results.select('.txtBoxStyle')
type(authors) # shows as list

len(authors) # shows as 328

type(authors[0]) # shows as bs4.element.Tag

# returns all authors
authors[0].getText()

authors[3].getText( # returns a specific author

# iterate over all authors and shows in pretty list layout
for author in authors:
    print(authors[0].getText())
