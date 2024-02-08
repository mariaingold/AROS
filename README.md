# AROS

AROS v 0.4  
Academic Research Online System  
Simple reflex agent web scraper  
Scrape specified arXiv pages for basic citation data, search for keyword (or phrase), and store results in a CSV file if the keyword is found  
Uses Python, requests, Beautiful Soup 4, Pandas  

## AUTHOR: Maria Ingold

UoEO MSc AI Intelligent Agents Development Individual Assignment  
Assignment date: 12 February, 2024  

## INSTRUCTIONS

### Installation

* Install [python](https://www.python.org/)
* To install libraries, first install [pip](https://pypi.org/project/pip/)
To install libraries, run the following commands one at a time.  
* pip install requests
* pip install beautifulsoup4
* pip install pandas
* pip install pyarrow

### Run

* Run python code in terminal: python AROS.py
* Manually change parameters in code. Can set: URL, keyword(s) and output file

### Output File Location

* This is stored in the directory where you are running Python in the terminal window. E.g. PS C:\Users\UserName

## TOOLS

From (Ingold et al., 2023):  

| Tool / Package                                                | Description                                        | Version used |
|:--------------------------------------------------------------|:---------------------------------------------------|:-------------|
| [GitHub](https://github.com/)                                 | Open-source version control system                 | 3.3.8 (x64)  |
| [Visual Studio Code](https://code.visualstudio.com/)          | Free source code editor (works with GitHub)        | 1.86.0       |
| [python](https://www.python.org/)                             | Programming language                               | 3.12.0       |
| [pip](https://pypi.org/project/pip/)                          | Python package installer                           | 24.0         |
| [requests](https://pypi.org/project/requests/)                | HTTP requests                                      | 2.32.0       |
| [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/)  | Web scraping and parse tree                        | 4.12.3       |
| [pandas](https://pypi.org/project/pandas/)                    | Data structures and analysis                       | 2.2.0        |
| [pyarrow](https://pypi.org/project/pyarrow/)                  | Future-proof dependency requirement for Pandas 3.0 | 15.0.0       |

## IMPLEMENTATION

### Version 0.1 Evaluated Scrapy versus requests / Beautiful Soup 4 / Pandas

* [Simple Scrapy (0.1)](https://github.com/mariaingold/scrape-arxiv-scrapy)
* Scrapy is generally for more complex systems.
* [Simple requests / Beautiful Soup 4 / Pandas (0.1)](https://github.com/mariaingold/scrape-arxiv-soup)
* requests / Beautiful Soup 4 / Pandas is better for learners and smaller systems, hence this was selected.

### Version 0.1: Very basic web scraper

#### Overview 0.1

* Summary: Simple web scraper
* Description: Scrapes a specific arXiv page for basic citation data and stores in a CSV file
* Technologies: Python, requests, Beautiful Soup 4, Pandas

#### Functionality

* Collection: (requests) arXiv selected as web page code can be extracted. Some pages prevented parsing. For the first version, it only extracted basic citation information from [https://arxiv.org/abs/2109.00656](https://arxiv.org/abs/2109.00656).

* Extraction: (Beautiful Soup 4) Extracted citation title, authors and date and placed it in a CSV file.
* Transformation: (Pandas) Created a dictionary of the data and converted it to a data frame.
* Store: (Pandas) data frame exported to a CSV file.

#### Limitations

* Format: This was very simply sequentially scripted in a single file without abstraction in terms of functions or classes.
* Limitations: Not modular. Only a single web page. Hardcoded URL. Limited data. No natural language processing. No user interface.

### Version 0.2: Modular, URL parameter, and now includes abstract

#### Changes from 0.1

* STEP 1: Move from a script to a class (modularity). Collects, extracts, transforms and stores citation data from an arXiv page. Created a single class as the process is simple, with only four methods. Instead of using separate classes for collect, extract, transform and store, they are each methods of the ArxivScraper class. This keeps it simple, but modular.
* STEP 2: Move from a hard-coded URL to a parameter (flexibility / reusability). Made the URL a parameter of the class, so that the class can be used to scrape any arXiv page. As this is now a class method, the URL can be a parameter of the method.
* STEP 3: Add citation abstract (completeness / extensibility). Moving beyond the basic citation data (title, auther, date), the scraper also now extracts the paper's abstract. This better enables the scraper to be used as a simple reflex agent, responding to the existence of a keyword in the title or abstract.

### Version 0.3 Simple reflex agent

#### Overview 0.3

* Create a simple reflex agent that responds to the existence of a keyword in the title or abstract.

#### Changes from 0.2

* STEP 1: Add a decide_relevance method to the ArxivScraper class.
* STEP 2: Add a run method to the ArxivScraper class with a keyword parameter.
* STEP 3: Change extract to only search for relevant data. Move dictionary to extract method.

### Version 0.4 Added pytest unit testing, multiple URLs, and error handling

* STEP 1: Add test_AROS.py which unit tests __init__, collect, extract, transform, store, decide_relevance, and run methods.
* STEP 2: Add capacity to test with more than one URL.
* STEP 3: Add basic error handling.

## REFERENCES

* Abodayeh, A. et al. (2023) Web Scraping for Data Analytics: A BeautifulSoup Implementation, Proceedings - 2023 6th International Conference of Women in Data Science at Prince Sultan University, WiDS-PSU 2023  65–69. DOI: [https://doi.org/10.1109/WIDS-PSU57071.2023.00025](https://doi.org/10.1109/WIDS-PSU57071.2023.00025).
* Amos, D. (2022) A Practical Introduction to Web Scraping in Python – Real Python. Available from: [https://realpython.com/python-web-scraping-practical-introduction/](https://realpython.com/python-web-scraping-practical-introduction/) [Accessed 10 December 2023].
* Breuss, M. (2022) How to Check if a Python String Contains a Substring. Available from: [https://realpython.com/python-string-contains-substring/](https://realpython.com/python-string-contains-substring/) [Accessed 5 February 2024].
* Ingold, M., Grimal, C. & Alaskar, A. (2023) Intelligent Agents: Development Team Project Report. Available from: [https://mariaingold.github.io/artefacts/2_IA_Team1_DevelopmentTeamProjectReport.pdf](https://mariaingold.github.io/artefacts/2_IA_Team1_DevelopmentTeamProjectReport.pdf) [Accessed 3 February 2024].
* Khder, M.A. (2021) Web Scraping or Web Crawling: State of Art, Techniques, Approaches and Application, Int J Advance Soft Compu Appl  13(3). DOI: [https://doi.org/10.15849/IJASCA.211128.11](https://doi.org/10.15849/IJASCA.211128.11).
* Microsoft (N.D.) Python Testing in Visual Studio Code. Available from: [https://code.visualstudio.com/docs/python/testing#_tests-in-pytest](https://code.visualstudio.com/docs/python/testing#_tests-in-pytest) [Accessed 6 February 2024].
* Nigam, H. & Biswas, P. (2021) Web Scraping: From Tools to Related Legislation and Implementation Using Python, Innovative Data Communication Technologies and Application  149–164. Available from: [https://doi.org/10.1007/978-981-15-9651-3_13](https://doi.org/10.1007/978-981-15-9651-3_13).
* Pandas (2024) Pandas Documentation. Available from: [https://pandas.pydata.org/docs/index.html](https://pandas.pydata.org/docs/index.html) [Accessed 4 February 2024].
* PyPi (N.D.) requests 2.31.0. Available from: [https://pypi.org/project/requests/](https://pypi.org/project/requests/) [Accessed 4 February 2024].
* Pytest (N.D.) How to use temporary directories and files in tests. Available from: [https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html](https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html) [Accessed 6 February 2024].
* Ramos, L.P. (2023) Python Classes: The Power of Object-Oriented Programming – Real Python. Available from: [https://realpython.com/python-classes/#getting-started-with-python-classes](https://realpython.com/python-classes/#getting-started-with-python-classes) [Accessed 4 February 2024].
* Stack Overflow (2016) Python : Web Scraping Specific Keywords. Available from: [https://stackoverflow.com/questions/40121232/python-web-scraping-specific-keywords](https://stackoverflow.com/questions/40121232/python-web-scraping-specific-keywords) [Accessed 5 February 2024].
* W3 Schools (N.D.) Python Try Except. Available from: [https://www.w3schools.com/python/python_try_except.asp](https://www.w3schools.com/python/python_try_except.asp) [Accessed 7 February 2024].
