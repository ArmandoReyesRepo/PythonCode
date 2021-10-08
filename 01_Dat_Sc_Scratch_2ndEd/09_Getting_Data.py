# -*- coding: utf-8 -*-
"""
Created on Sun May 30 01:16:01 2021

@author: arman
"""

"""  Use of egrep """
""" This is with the use of pipe """
""" This is used within the command line of linux """
""" //  cat tab_delimited_stock_prices.txt | python3 egrep.py "[0-9]" | python3 line_count3.py ///  """

# egrep.py
import sys, re

if __name__ == "__main__":

    # sys.argv is the list of command-line arguments
    # sys.argv[0] is the name of the program itself
    # sys.argv[1] will be the regex specfied at the command line
    regex = sys.argv[1]

    # for every line passed into the script
    for line in sys.stdin:
        # if it matches the regex, write it to stdout
        if re.search(regex, line):
            sys.stdout.write(line)
            

""" Use of line count """
# line_count.py
import sys

if __name__ == "__main__":

    count = 0
    for line in sys.stdin:
        count += 1

    # print goes to sys.stdout
    print (count)
    
"""  Use of most commong words in a file """
"""  cat stocks.txt | python3 most_common_words3.py 10   """

# most_common_words.py
import sys
from collections import Counter

if __name__ == "__main__":

    # pass in number of words as first argument
    try:
        num_words = int(sys.argv[1])
    except:
        print ("usage: most_common_words3.py num_words")
        sys.exit(1)   # non-zero exit code indicates error

    counter = Counter(word.lower()                      
                      for line in sys.stdin             
                      for word in line.strip().split()  
                      if word)                          
            
    for word, count in counter.most_common(num_words):
        sys.stdout.write(str(count))
        sys.stdout.write("\t")
        sys.stdout.write(word)
        sys.stdout.write("\n")
        

"""  Getting the domains of emails  """

def get_domain(email_address: str) -> str:
    """Split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]

"""  Doing some examples """
# a couple of tests
assert get_domain('joelgrus@gmail.com') == 'gmail.com'
assert get_domain('joel@m.datasciencester.com') == 'm.datasciencester.com'



"""  Testing getting mails from a file in directory indicated """
import os
path = os.getcwd()
print(path)
os.chdir('C:\\Users\\arman\\OneDrive\\Desktop\\2020\\08_DataScienceFromScratch\\data-science-from-scratch-master\\first-edition\\code')
path=os.getcwd()
print(path)        
os.listdir(path)


from collections import Counter

with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line)


"""  Delimited files """

"""  Getting delimited tab data """


def process(date: str, symbol: str, closing_price: float) -> None:
    # Imaginge that this function actually does something.
    assert closing_price > 0.0

import csv

"""  Creating the file tab_delimited_stock_prices.txt"""

with open('tab_delimited_stock_prices.txt', 'w') as f:
    f.write("""6/21/2014\tAAPL\t90.91
6/21/2014\tMSFT\t41.68
6/21/2014\tFB\t64.5
6/19/2014\tAAPL\t91.86
6/19/2014\tMSFT\t41.51
6/19/2014\tFB\t64.34
""")


""" Getting the last row of the tab_delimited_file """
with open('tab_delimited_stock_prices.txt') as f:
    tab_reader = csv.reader(f, delimiter='\t')
    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)
        
""" Using the first line as the header with dictionaries with colon separated files """

with open('colon_delimited_stock_prices.txt', 'w') as f:
    f.write("""date:symbol:closing_price
6/20/2014:AAPL:90.91
6/20/2014:MSFT:41.68
6/20/2014:FB:64.5
""")

""" Getting the last elementt with dictionaries""""
with open('colon_delimited_stock_prices.txt') as f:
    colon_reader = csv.DictReader(f, delimiter=':')
    for dict_row in colon_reader:
        date = dict_row["date"]
        symbol = dict_row["symbol"]
        closing_price = float(dict_row["closing_price"])
        process(date, symbol, closing_price)
        
""" Using comma separated files """

todays_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5 }

with open('comma_delimited_stock_prices.txt', 'w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    for stock, price in todays_prices.items():
        csv_writer.writerow([stock, price])
    

"""  Scrapping web data using Web Scrapping """

from bs4 import BeautifulSoup
import requests

# I put the relevant HTML file on GitHub. In order to fit
# the URL in the book I had to split it across two lines.
# Recall that whitespace-separated strings get concatenated.
url = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')
first_paragraph = soup.find('p')        # or just soup.p
assert str(soup.find('p')) == '<p id="p1">This is the first paragraph.</p>'
first_paragraph_text = soup.p.text
first_paragraph_text
first_paragraph_words = soup.p.text.split()
first_paragraph_words
assert first_paragraph_words == ['This', 'is', 'the', 'first', 'paragraph.']

first_paragraph_id = soup.p['id']       # raises KeyError if no 'id'
first_paragraph_id

first_paragraph_id2 = soup.p.get('id')
first_paragraph_id2

assert first_paragraph_id == first_paragraph_id2 == 'p1'

all_paragraphs = soup.find_all('p')  # or just soup('p')
all_paragraphs

paragraphs_with_ids = [p for p in soup('p') if p.get('id')]
paragraphs_with_ids

assert len(all_paragraphs) == 2
assert len(paragraphs_with_ids) == 1

"""  Fingind paragraphs with a specific class """

important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])]
