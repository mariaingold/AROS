# AROS v 0.2 (Academic Research Online System)
# Aiming towards a simple reflex agent web scraper
# Scrapes a specific arxiv page for basic citation data and stores in a CSV file
# Uses Python, requests, Beautiful Soup 4, Pandas 
#
# Version 0.1: A simple prototype script that collected, extracted, transformed and stored citation data from a hardcoded arXiv page.
# Version 0.2: Three steps to build on 0.1. 1) Move the script into a class, ArxivScraper, with methods for each of the four steps. 2) Move URL to a parameter. 3) Add abstract.
#
# Author: Maria Ingold
# Built as part of UoEO MSc AI Intelligent Agents assignment
# Date: 12 February 2023 (Assignment due date)

import requests
from bs4 import BeautifulSoup
import pandas as pd

# STEP 1: MOVE FROM A SCRIPT TO A CLASS (MODULARITY)
# ArxivScraper class
# Collects, extracts, transforms and stores citation data from an arXiv page
# Created a single class as the process is simple, with only four methods. (Ramos, 2023)
# Instead of using separate classes for collect, extract, transform and store, they are each methods of the ArxivScraper class. 
# This keeps it simple, but modular. 
# Class references: (Ramos, 2023)

class ArxivScraper:
    # Initialises the instance with the URL and sets the other variables to None
    def __init__(self, url):
        self.url = url                      # The URL of the arXiV page to scrape
        self.page_content = None            # The content of the page being scraped  
        self.soup = None                    # The parsed HTML content of the page
        self.citation_title = None          # The title of the paper
        self.citation_authors = None        # The authors of the paper (one or more)
        self.citation_date = None           # The date of the paper
        self.citation_abstract = None       # The abstract of the paper (STEP 3: ADD ABSTRACT)
        self.data = None                    # The citation data as a dictionary (required for conversion to a Pandas DataFrame)
        self.df = None                      # The citation data as a Pandas DataFrame

    # COLLECT  
    def collect(self):
        # STEP 2: MOVE FROM A HARD-CODED URL TO A PARAMETER (FLEXIBILITY / REUSABILITY)
        # Wanted to make the URL a parameter of the class, so that the class can be used to scrape any arXiv page. 
        # As this is now a class method, the URL can be a parameter of the method.
        # Why requests? It simplifes HTTP requests and it is less verbose and more intiutive than urllib. (Amos, 2022)
        # requests references: (Nigam & Biswas, 2021; Abodayeh et al., 2023; PyPi, N.D.)
        page = requests.get(self.url)       # Get the page content   
        self.page_content = page.content    # Set the page content variable to the content of web page (in bytes)

    # EXTRACT
    def extract(self):
        # STEP 3: ADD CITATION ABSTRACT (COMPLETENESS / EXTENSIBILITY)
        # Moving beyond the basic citation data (title, auther, date), the scraper also now extracts the paper's abstract.
        # This better enables the scraper to be used as a simple reflex agent, responding to the existence of a keyword in the title or abstract.
        # Why BeautifulSoup 4? It is simple for extracting HTML, good for beginners, and can navigate, search and modify the parse tree.
        # BeautifulSoup 4 refrences: (Khder, 2021; Amos, 2022; Abodayeh et al., 2023)
        self.soup = BeautifulSoup(self.page_content, "html.parser") # Parse the webpage content
        #print (self.soup.prettify())       # Print the HTML contents of the page
        #print(self.soup.get_text())        # Print the text of the page
        # Extract the citation title
        meta_tag = self.soup.find("meta", attrs={"name": "citation_title"})                 
        self.citation_title = meta_tag["content"] if meta_tag else "No meta title given"
        print(self.citation_title) 
        # Extract the citation author(s)    
        meta_tags = self.soup.find_all("meta", attrs={"name": "citation_author"})           
        self.citation_authors = [tag["content"] for tag in meta_tags if tag] if meta_tag else "No meta author given" 
        print(self.citation_authors)
        # Extract the citation date
        meta_tag = self.soup.find("meta", attrs={"name": "citation_date"})
        self.citation_date = meta_tag["content"] if meta_tag else "No meta date given"
        print(self.citation_date)
        # Extract the citation abstract
        meta_tag = self.soup.find("meta", attrs={"name": "citation_abstract"})
        self.citation_abstract = meta_tag["content"] if meta_tag else "No meta abstract given"
        print(self.citation_abstract)   

    # TRANSFORM
    def transform(self):
        # CREATE A PYTHON DICTIONARY (KEY:VALUE PAIRS) AND CONVERT TO A PANDAS DATAFRAME
        # Why Pandas? Data analysis and manipulation, in Python, without having to switch languages.
        # Pandas usage: (Nigam & Biswas, 2021; pandas, 2024))
        # Create a python dictionary
        self.data = {
            "Title": [self.citation_title],
            "Authors": ["; ".join(self.citation_authors)],
            "Date": [self.citation_date],
            "Abstract": [self.citation_abstract]
        }
        # Convert the dictionary to a pandas DataFrame
        self.df = pd.DataFrame(self.data)

    # STORE
    def store(self, filename):
        # EXPORT THE DATAFRAME TO A CSV FILE (USING PANDAS)
        self.df.to_csv(filename, index=False)

# USAGE
scraper = ArxivScraper("https://arxiv.org/abs/2109.00656") # Create an instance of the ArxivScraper class with the URL as a parameter
scraper.collect()                           # Collect the page content
scraper.extract()                           # Extract the citation data
scraper.transform()                         # Transform the citation data
scraper.store("citation_data.csv")          # Store the citation data in a CSV file
