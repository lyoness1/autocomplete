# autocomplete
This is an app I wrote to learn about Python's `os` module and trie data structures' creation and retrieval. 

When the server starts, the `get_files.py` file queries your local machine for all files and directories from the current directory downward. After scanning for files, `get_files.py` adds all the filepath strings to the prefix trie in the `trie.py` file and caches the trie on the server. When you type a prefix into the box in the browswer, it populates a list of autocomplete options from the prefix trie cached on the server. 

### To Run
1. Clone this repo locally and make sure Python 2.7 is installed
2. `$ virtualenv env` to set-up a virtual environment
3. `$ source env/bin/activate` to activate virtual environment
4. `$ pip install -r requirements.txt` to install dependencies
5. `$ python server.py` to start the application
6. Navigate to http://127.0.0.1:5000/ in a browser. 
7. Enter any prefix into the box to see local files containing that prefix. 
