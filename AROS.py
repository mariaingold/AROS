# AROS v 0.3 (Academic Research Online System)
# Simple reflex agent web scraper
# Scrapes a specific arxiv page for basic citation data and stores in a CSV file
# Uses Python, requests, Beautiful Soup 4, Pandas 
# 
# USAGE: python AROS_v0.3.py
# INPUT: URL of the arXiv page to scrape (input into the ArxivScraper class instance)
# OUTPUT: CSV file with the citation data 
#
# Version 0.1: A simple prototype script that collected, extracted, transformed and stored citation data from a hardcoded arXiv page.
# Version 0.2: Increase modularity and flexibility with 3 changes:
#   STEP 1: Move the script into a class, ArxivScraper, with methods to collect, extract, transform and store. 
#   STEP 2: Move URL to a parameter. 
#   STEP 3: Add abstract.
# Version 0.3: Create a simple reflex agent that responds to the existence of a keyword in the title or abstract.
#   STEP 1: Add a decide_relevance method to the ArxivScraper class.
#   STEP 2: Add a run method to the ArxivScraper class with a keyword parameter.
#   STEP 3: Change extract to only search for relevent data. Move dictionary to extract method.
# Author: Maria Ingold
# Built as part of UoEO MSc AI Intelligent Agents assignment
# Date: 12 February 2023 (Assignment due date)

import requests
from bs4 import BeautifulSoup
import pandas as pd

# V0.2 STEP 1: MOVE FROM A SCRIPT TO A CLASS (MODULARITY)
# ArxivScraper class
# Collects, extracts, transforms and stores citation data from an arXiv page
# Created a single class as the process is simple, with only four methods. (Ramos, 2023)
# Instead of using separate classes for collect, extract, transform and store, they are each methods of the ArxivScraper class. 
# This keeps it simple, but modular. 
# Class references: (Ramos, 2023)

class ArxivScraper:
    # V0.2 STEP 1: Initialise the instance with the URL and sets the other variables to None
    # V0.3 STEP 2: Remove instance variables that are only used locally and make local instead. 
    def __init__(self, url):
        self.url = url                      # The URL of the arXiV page to scrape
        self.page_content = None            # The content of the page being scraped  
        self.data = None                    # The citation data as a dictionary (required for conversion to a Pandas DataFrame)
        self.df = None                      # The citation data as a Pandas DataFrame

    # COLLECT  
    # V0.1 STEP 1: COLLECT THE PAGE CONTENT (USING REQUESTS)
    # V0.2 STEP 2: MOVE FROM A HARD-CODED URL TO A PARAMETER (FLEXIBILITY / REUSABILITY) AND MAKE IT A CLASS METHOD (MODULARITY)
    # Why Requests? It simplifes HTTP requests and it is less verbose and more intiutive than urllib. (Amos, 2022)
    # Why a URL parameter? So the class can simply scrape any arXiv page. As this is now a class method, the URL can be a parameter of the method.
    # Requests references: (Nigam & Biswas, 2021; Abodayeh et al., 2023; PyPi, N.D.)
    def collect(self):
        page = requests.get(self.url)       # Get the page content   
        self.page_content = page.content    # Set the page content variable to the content of web page (in bytes)

    # EXTRACT
    # V0.1 STEP 2: EXTRACT THE CITATION TITLE, AUTHOR, AND DATE (USING BEAUTIFULSOUP 4)
    # V0.2 STEP 3: ADD EXTRACTION OF CITATION ABSTRACT (COMPLETENESS / EXTENSIBILITY) AND MAKE IT A CLASS METHOD (MODULARITY)
    # V0.3 STEP 3: MOVE DICTIONARY TO EXTRACT METHOD. TRANSFORM SHOULD JUST CONVERT.
    # Why BeautifulSoup 4? It is simple for extracting HTML, good for beginners, and can navigate, search and modify the parse tree.
    # Why abstract? Better enables the scraper to be used as a simple reflex agent, responding to the existence of a keyword in the title or abstract.
    # BeautifulSoup 4 references: (Khder, 2021; Amos, 2022; Abodayeh et al., 2023)       
    def extract(self):
        soup = BeautifulSoup(self.page_content, "html.parser") # Parse the webpage content
        #print(soup.prettify())       # Print the HTML contents of the page
        #print(soup.get_text())        # Print the text of the page
        # Extract the citation title
        meta_tag = soup.find("meta", attrs={"name": "citation_title"})                 
        title = meta_tag["content"] if meta_tag else "No meta title given"
        # print(title) 
        # Extract the citation author(s)    
        meta_tags = soup.find_all("meta", attrs={"name": "citation_author"})           
        authors = [tag["content"] for tag in meta_tags if tag] if meta_tag else "No meta author given" 
        # print(authors)
        # Extract the citation date
        meta_tag = soup.find("meta", attrs={"name": "citation_date"})
        date = meta_tag["content"] if meta_tag else "No meta date given"
        # print(date)
        # Extract the citation abstract
        meta_tag = soup.find("meta", attrs={"name": "citation_abstract"})
        abstract = meta_tag["content"] if meta_tag else "No meta abstract given"
        # print(abstract)  
        # Create a python dictionary
        self.data = {
            "Title": title,
            "Authors": "; ".join(authors),
            "Date": date,
            "Abstract": abstract
        } 

    # TRANSFORM
    # V0.1 CREATE A PYTHON DICTIONARY (KEY:VALUE PAIRS) AND CONVERT TO A PANDAS DATAFRAME
    # V0.2 MAKE IT A CLASS METHOD (MODULARITY)
    # V0.3 STEP 3: MOVE DICTIONARY TO EXTRACT METHOD. TRANSFORM SHOULD JUST CONVERT.
    # Why Pandas? Data analysis and manipulation, in Python, without having to switch languages.
    # Pandas references: (Nigam & Biswas, 2021; Pandas, 2024))
    def transform(self):
        # Convert the dictionary to a pandas DataFrame
        self.df = pd.DataFrame([self.data])

    # STORE
    # V0.1 EXPORT THE DATAFRAME TO A CSV FILE (USING PANDAS)
    # V0.2 MAKE IT A CLASS METHOD (MODULARITY)
    def store(self, filename):
        self.df.to_csv(filename, index=False)

    # DECIDE RELEVANCE 
    # V0.3 STEP 1: ADD A METHOD TO DECIDE RELEVANCE BASED ON A KEYWORD
    def decide_relevance(self, title, abstract, keyword):
        return keyword.lower() in title.lower() or keyword.lower() in abstract.lower()

    # RUN
    # V0.3 STEP 2: ADD MAIN LOGIC OF THE AGENT
    def run(self, keyword, filename):
        self.collect()
        self.extract()
        print(f"Keyword: '{keyword}' in {self.url}") 
        if self.decide_relevance(self.data["Title"], self.data["Abstract"], keyword):
            print(f"Relevant!\nTitle: {self.data['Title']}\nDate: {self.data['Date']}\nAuthors: {self.data['Authors']}\nAbstract: {self.data['Abstract']}")
            self.transform()
            self.store(filename)
        else:
            print("Not relevant. No data stored.")

# USAGE
# V0.2: ADD A CLASS INSTANCE AND CALL THE METHODS
# V0.3: USE A RUN METHOD TO CALL THE METHODS 
scraper = ArxivScraper("https://arxiv.org/abs/2109.00656")  # Create ArxivScraper class instance with URL parameter - will find
# scraper = ArxivScraper("https://arxiv.org/abs/2402.01499")  # Create ArxivScraper class instance with URL parameter - won't find
# scraper = ArxivScraper("https://arxiv.org/abs/2109")        # Create ArxivScraper class instance with URL parameter - won't find
scraper.run("web scraping", "citation_data_0.6.csv")        # Run the scraper with a keyword and output filename