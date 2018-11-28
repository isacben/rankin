# Readme

This is a python scirpt that googles a keyword phrase and tries to find a blog post from a given website in the first page of the Google search results. It works by scraping this results page.

<h2>Requirements</h2>

This script needs the following requirements:

* Python 3
* requests python module
* beautifulsoup4 module

<h2>Installation</h2>

To use the scritp, first install the requests module and the beaturifulsoup4 module.

Run the following command to install the requests module:

<pre>python3 -m pip install requests</pre>

Run the following command ton install beatufulsoup4:

<pre>python3 -m pip install beautifulsoup4</pre>

<h2>Usage</h2>

Place the rankin.py script wherever you want in your filesystem. Then run the script as follows:

<code>python3 rankin.py yourwebsite.com keyword phrase</code>

The script receives two parameters:

* A target website: the script will check if the search results have any post from the target website.
* A keyword prase: the keyword phrase is what you would type in the google search box.
