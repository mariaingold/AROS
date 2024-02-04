# AROS
AROS v 0.2  
Academic Research Online System 
Simple reflex agent web scraper  
Scrapes a specific arxiv page for basic citation data and stores in a CSV file  
Uses Python, requests, Beautiful Soup 4, Pandas   

# AUTHOR: Maria Ingold
UoEO MSc AI Intelligent Agents Development Individual Assignment  
Assignment date: 12 February, 2024  

# INSTRUCTIONS
How to execute the code  

# TOOLS

From (Ingold et al., 2023):  

| Tool / Package	                                            | Description                                   |
|:--------------------------------------------------------------|:----------------------------------------------|
| [GitHub](https://github.com/)                                 | Open-source version control system            |
| [Visual Studio Code](https://code.visualstudio.com/)          | Free source code editor (works with GitHub)   |
| [python](https://www.python.org/)                             | Programming language                          |
| [pip](https://pypi.org/project/pip/)                          ! Python package installer                      |
| [requests](https://pypi.org/project/requests/)                | HTTP requests                                 |
| [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/)  | Web scraping and parse tree                   |
| [pandas](https://pypi.org/project/pandas/)                    | Data structures and analysis                  |

# IMPLEMENTATION
## Version 0.1 Evaluated Scrapy versus requests / Beautiful Soup 4 / Pandas
* https://github.com/mariaingold/scrape-arxiv-scrapy
* Scrapy is generally for more complex systems. 
* https://github.com/mariaingold/scrape-arxiv-soup 
* requests / Beautiful Soup 4 / Pandas is better for learners and smaller systems, hence this was selected. 
## Version 0.1: Very basic webscraper 
### Overview
* Summary: Simple web scraper
* Description: Scrapes a specific arxiv page for basic citation data and stores in a CSV file  
* Technologies: Python, requests, Beautiful Soup 4, Pandas  
### Functionality
* Collection: (requests) Arxiv selected as web page code can be extracted. Some pages prevented parsing. For the first version, it only extracted basic citation information from https://arxiv.org/abs/2109.00656.  
* Extraction: (Beautiful Soup 4) Extracted citation title, authors and date and placed it in a CSV file. 
* Transformation: (Pandas) Created a dictionary of the data and converted it to a data frame.
* Store: (Pandas) data frame exported to a CSV file.
### Limitations 
* Format: This was very simply sequentially scripted in a single file without abstraction in terms of functions or classes.
* Limitations: Not modular. Only a single web page. Hardcoded URL. Limited data. No natural language processing. No user interface.
## Version 0.2: Modular, URL parameter, and now includes abstract
### Changes
* STEP 1: Move from a script to a class (modularity). Collects, extracts, transforms and stores citation data from an arXiv page. Created a single class as the process is simple, with only four methods. Instead of using separate classes for collect, extract, transform and store, they are each methods of the ArxivScraper class. This keeps it simple, but modular. 
* STEP 2: Move from a hard-coded URL to a parameter (flexibility / reusability). Made the URL a parameter of the class, so that the class can be used to scrape any arXiv page. As this is now a class method, the URL can be a parameter of the method.
* STEP 3: Add citation abstract (completeness / extensibility). Moving beyond the basic citation data (title, auther, date), the scraper also now extracts the paper's abstract. This better enables the scraper to be used as a simple reflex agent, responding to the existence of a keyword in the title or abstract.

# REFERENCES
* Abodayeh, A. et al. (2023) Web Scraping for Data Analytics: A BeautifulSoup Implementation, Proceedings - 2023 6th International Conference of Women in Data Science at Prince Sultan University, WiDS-PSU 2023  65–69. DOI: https://doi.org/10.1109/WIDS-PSU57071.2023.00025.
* Amos, D. (2022) A Practical Introduction to Web Scraping in Python – Real Python. Available from: https://realpython.com/python-web-scraping-practical-introduction/ [Accessed 10 December 2023].
* Ingold, M., Grimal, C. & Alaskar, A. (2023) Intelligent Agents: Development Team Project Report. Available from: https://mariaingold.github.io/artefacts/2_IA_Team1_DevelopmentTeamProjectReport.pdf [Accessed 3 February 2024].
* Khder, M.A. (2021) Web Scraping or Web Crawling: State of Art, Techniques, Approaches and Application, Int J Advance Soft Compu Appl  13(3). DOI: https://doi.org/10.15849/IJASCA.211128.11.
* Nigam, H. & Biswas, P. (2021) Web Scraping: From Tools to Related Legislation and Implementation Using Python, Innovative Data Communication Technologies and Application  149–164. Available from: https://doi.org/10.1007/978-981-15-9651-3_13.
* pandas (2024) pandas documentation. Available from: https://pandas.pydata.org/docs/index.html [Accessed 4 February 2024].
* PyPi (N.D.) requests 2.31.0. Available from: https://pypi.org/project/requests/ [Accessed 4 February 2024].
* Ramos, L.P. (2023) Python Classes: The Power of Object-Oriented Programming – Real Python. Available from: https://realpython.com/python-classes/#getting-started-with-python-classes [Accessed 4 February 2024].
 
