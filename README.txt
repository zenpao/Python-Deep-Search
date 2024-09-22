Hello and welcome to using the searchdocument script.

1) Run the script by entering cmd in the URL bar of the folder you are in.
You can also do the long way by opening cmd and navigating to the folder where the script is at.


2) Before you continue, know that "searchdocument_2param.py / searchdocument_3param.py" are the same codes with the latter being able to have one more extra parameter for searching accurately. Choose whichever you prefer and run one instance by entering "python searchdocument_2param.py" or "python searchdocument_3param.py". Just follow the instructions how to search.

3) After you you received the results of either from searchdocument_2param.py / searchdocument_3param.py .
It will yield a "search_results.txt" with possible list of matched results. 

4) If results are too many, you can use "searchdocument_resultconverter.py" to convert each line into hyperlinks, for you to be able to check each local file one by one using the browser as a trigger. Just enter "python searchdocument_resultsconverter.py" in the cmd.

That's it!


----
Just a note, pip install the following if it does not work:
os
fnmatch
tqdm
BeautifulSoup
bs4
chardet
pdfplumber
PyPDF2
textract