# test ArxivScraper.py
# Name file test_AROS.py, as Visual Studio Code can be configured to run all files with the test_ prefix as tests. (Microsoft, N.D.)
# Pytest seems to be the default testing framework for Python and could not get unittest to work. (Pytest, N.D.)
# Run: These tests can be run with the command: pytest test_AROS.py or using the pytest extension in Visual Studio Code. (Microsoft, N.D.)
#
# NOTES
# Note: The tests are not exhaustive, but they cover the main methods of the ArxivScraper class.
# Note: The tests are run in the order they are defined in the file. But they can be run one at a time in any order.
# Note: The tests returned a warning for a deprecated datetime format. This is not an issue with the code, but with one of the libraries. 
#       Checked libraries using pip show. Pandas was on 2.1.1 (now 2.2.0). Beautiful Soup 4 was on 4.12.2 (now 4.12.3). Requests was on 2.31.0 (same version).
#       The warning is still there until (probably) Pandas is updated.
# Note: Another warning was added about a future version of Pandas 3.0 requiring pyarrow. 
#       Did pip install pyarrow. The warning is gone.
# Note: After installing pytest, my GitHub Desktop AROS directory included a number of temporary and cache files and folders.
#       To ensure these were not added to my repository, I added a .gitignore file to ignore the following: .pytest_cache/, .vscode/, __pycache__/
#
# Author: Maria Ingold
# Built as part of UoEO MSc AI Intelligent Agents assignment
# Date: 12 February 2023 (Assignment due date)

import pytest
from AROS import ArxivScraper

# Test URL: https://arxiv.org/abs/2109.00656
# Title: Developing Products Update-Alert System for e-Commerce Websites Users Using HTML Data and Web Scraping Technique
# Date: 2021/09/02
# Authors: Onyenwe, Ikechukwu; Onyedinma, Ebele; Nwafor, Chidinma; Agbata, Obinna
# Abstract: Websites are regarded as domains of limitless information which anyone and everyone can access. The new trend of technology put us to change the way we are doing our business. The Internet now is fastly becoming a new place for business and the advancement in this technology gave rise to the number of e-commerce websites. This made the lifestyle of marketers/vendors, retailers and consumers (collectively regarded as users in this paper) easy, because it provides easy platforms to sale/order items through the internet. This also requires that the users will have to spend a lot of time and effort to search for the best product deals, products updates and offers on e-commerce websites. They have to filter and compare search results by themselves which takes a lot of time and there are chances of ambiguous results. In this paper, we applied web crawling and scraping methods on an e-commerce website to get HTML data for identifying products updates based on the current time. The HTML data is preprocessed to extract details of the products such as name, price, post date and time, etc. to serve as useful information for users.

# Test the __init__ method with a good URL. urls is a required parameter. The other variables are set to None.
def test_init():
    urls = ["https://arxiv.org/abs/2109.00656"]
    scraper = ArxivScraper(urls)
    assert scraper.urls == urls
    assert scraper.page_content == None
    assert scraper.data == None
    assert scraper.df == None

# Test the collect method with a good URL. The page content should no longer be None after collecting.
def test_collect():
    urls = ["https://arxiv.org/abs/2109.00656"]
    scraper = ArxivScraper(urls)
    scraper.collect(urls[0])
    assert scraper.page_content != None

# Test the extract method with a good URL. The data should no longer be None after extracting.
def test_extract():
    urls = ["https://arxiv.org/abs/2109.00656"]
    scraper = ArxivScraper(urls)
    scraper.collect(urls[0])
    scraper.extract()
    assert scraper.data != None

# Test the transform method with a good URL. The dataframe should no longer be empty after transforming.
def test_transform():
    urls = ["https://arxiv.org/abs/2109.00656"]
    scraper = ArxivScraper(urls)
    scraper.collect(urls[0])
    scraper.extract()
    scraper.transform()
    assert not scraper.df.empty         # Can test dataframes not empty, but not != None as the truth value is ambiguous (Pandas, 2023).

# Test the store method with a good URL. A file should be created after storing the dataframe.
def test_store(tmp_path):
    urls = ["https://arxiv.org/abs/2109.00656"]
    scraper = ArxivScraper(urls)
    scraper.collect(urls[0])
    scraper.extract()
    scraper.transform()
    filename = tmp_path / "test.csv"    # Create a temporary file for testing using the tmp_path fixture (Pytest, N.D.). 
    scraper.store(filename)
    assert filename.exists()

# Test the decide_relevance method with a good URL. The keyword "machine learning" is not in the title or abstract, so it should return False. The keyword "web scraping" is in the title, so it should return True.
def test_decide_relevance():
    urls = ["https://arxiv.org/abs/2109.00656"]
    scraper = ArxivScraper(urls)
    scraper.collect(urls[0])
    scraper.extract()
    keyword = "machine learning"
    assert scraper.decide_relevance(scraper.data["Title"], scraper.data["Abstract"], keyword) == False
    keyword = "web scraping"
    assert scraper.decide_relevance(scraper.data["Title"], scraper.data["Abstract"], keyword) == True

# Test the run method with a good URL. The keyword "web scraping" is in the title, so it should create a file.
def test_run(tmp_path):
    urls = ["https://arxiv.org/abs/2109.00656"]
    scraper = ArxivScraper(urls)
    keyword = "web scraping"
    filename = tmp_path / "test.csv"
    scraper.run(keyword, filename)
    assert filename.exists() 