# Readme

This is a python scirpt googles a keyword and tries to find a blog post from a given website in the search results. It works by scrap\ping the Google serach results first page.

Requirements:

* Python 3
* requests python module
* beautifulsoup4

Installation

To use the scritp, first install the requests module and the beaturifulsoup4 module.

Run the following command to install the requests module:

<code>python3 -m pip install requests</code>

Run the following command ton install beatufulsoup4:

<code>python3 -m pip install beautifulsoup4</code>

Usage

Place the rankin.py script wherever you want in your filesystem. Then run the script as follows:

<code>python3 rankin.py yourwebsite.com keyword phrase</code>

The script receives two parameters:

* A target website: the script will check if the search results have any post from the target website.
* A keyword prase: the keyword phrase is what you would type in the google search box.
