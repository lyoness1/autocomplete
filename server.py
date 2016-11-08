from flask import Flask, render_template, request, jsonify
import os
from trie import *
from get_files import *

app = Flask(__name__)

# pre-populate file cache as soon as app launches
_file_trie = FileTrie()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch')
def fetch_files():
    prefix = request.args.get('prefix')
    if prefix:
        return jsonify(_file_trie.get_all_with_prefix(prefix))
    else:
        return None


if __name__ == '__main__':
    # app.debug = True
    
    app.run()

    
    
