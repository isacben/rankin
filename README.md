# ranking.py

This is a python scirpt that googles a keyword phrase and tries to find a blog post from a given website in the first page of the Google search results. It works by scraping this results page.

Its pourpose is to quickly see if your blog post is ranking in the first page of Google for a specific search phrase.

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

Place the ranking.py script wherever you want in your filesystem.

<h2>Usage</h2>

Run the script as follows:

<pre>python3 ranking.py yourwebsite.com keyword phrase</pre>

The script receives two parameters:

* A target website: the script will check if the search results have any post from the target website.
* A keyword prase: the keyword phrase is what you would type in the google search box.

Example:

<pre>python3 ranking.py http://makethatbeat.com can midi keyboards play without computer</pre>

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

The website parameter must have the same format that Google registers in the search results. To know what the format of your target website name is, use the following command in the Google search bar:

<pre>site:yourwebsite.com</pre>

<h2>Warning</h2>

Be careful. Do not overuse this script. If you run it too many times, Google will notice and you will be blocked. The script will get a 503 (server error) error for certain time.

<h2>Disclaimer</h2>

This script was developed just for education pourposes. I do not promote the usage of this script for any other reason than that. I am not using the script for any other reason than education. I am not responsible of how anyone uses this script.
