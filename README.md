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

<pre>python3 rankin.py yourwebsite.com keyword phrase</pre>

The script receives two parameters:

* A target website: the script will check if the search results have any post from the target website.
* A keyword prase: the keyword phrase is what you would type in the google search box.

Example:

python3 ranking.py http://makethatbeat.com can midi keyboards play without computer

The output of the script will be similar to the following one, if a post was found:

<pre>
Target website: makethatbeat.com
Googling 'can midi keyboards play without computer'...
I found makethatbeat.com/play-without-computer/ in position 8
</pre>

The output will be similar to the following one, if no post was found:

<pre>
Target website: makethatbeat.com
Googling 'how to play a midi keyboard'...
No post was found...
</pre>

<h2>Important</h2>

The website parameter must have the same format the Google registers in the search results. To know what the format of your target website name is, use the following command in the Google search bar:

<pre>site:yourwebsite.com</pre>
