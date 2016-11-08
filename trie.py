import os

class Trie(object):
    """Trie object."""

    def __init__(self):
        """Initialize the Trie object."""
        self.root = Node()

    def insert(self, word):
        """Inserts a word into the trie."""
        self.root.__insert__(word)
        
    def get_all(self):
        """Returns a list of all complete words that were added to the trie."""
        return self.root.__get_all__()

    def get_all_with_prefix(self, prefix, string_pos=0):
        """Returns a list of possible words with given prefix."""
        return self.root.__get_all_with_prefix__(prefix, string_pos)
        
        

class Node(object):
    """Node for Trie."""
    
    def __init__(self):
        """Initialize the node."""

        self.word = None  # placeholder, for determining ends of full words
        self.nodes = {} # dict of nodes
        
    def __get_all__(self):
        """Get all of the words in the trie initiating at this node."""

        # initialize stack to store output
        ret = []
        
        # when leaf node of word is found, append to output
        for key, node in self.nodes.iteritems(): 
            if(node.word is not None):
                ret.append(node.word)
            # continue searching for words further down trie
            ret.extend(node.__get_all__())
                
        return ret
    
    def __str__(self):
        """if a node contains a word, print that word"""
        return self.word
    
    def __insert__(self, word, string_pos=0):
        """Add a word to the node in a Trie"""

        current_letter = word[string_pos]
        
        # Create the Node if it does not already exist
        if current_letter not in self.nodes:
            self.nodes[current_letter] = Node();

        # base case: end of word -> mark the end node's word as completed
        if(string_pos + 1 == len(word)):
            self.nodes[current_letter].word = word

        # progress: recurse with next character in word
        else:
            self.nodes[current_letter].__insert__(word, string_pos + 1)
            
        return True
    
    def __get_all_with_prefix__(self, prefix, string_pos):
        """Return sub-node trie of possible words for trie with given prefix."""

        ret = []
        
        for key, node in self.nodes.iteritems(): 
            # If the current character of the prefix is one of the nodes,
            # or the prefix match is already satisfied, then get the matches.
            if(string_pos >= len(prefix) or key == prefix[string_pos]):
                # found a word -> append to output
                if(node.word is not None):
                    ret.append(node.word)
                # if there are children...
                if(node.nodes != {}):
                    # if the prefix hasn't yet been completed, 
                    # continue through the prefix
                    if(string_pos + 1 <= len(prefix)):
                        ret.extend(node.__get_all_with_prefix__(prefix,
                                                                string_pos + 1))
                    # if no more prefix, find remaining words in sub-trie 
                    else:
                        ret.extend(node.__get_all_with_prefix__(prefix,
                                                                string_pos))
    
        return ret 



if __name__ == '__main__':

    trie = Trie()
    words = ["go", "gone", "gi", "cool", "comb", "grasshopper", "home", "hope", "hose"]
    [trie.insert(word) for word in words]

    for word in words:
        print "'" + word + "'", "added to trie"
        trie.insert(word)

    print "Make sure that the data structure is correctly set up by accesing words manually: "
    print str(trie.root.nodes['g'].nodes['o'])
    print str(trie.root.nodes['g'].nodes['i'])
    print str(trie.root.nodes['c'].nodes['o'].nodes['o'].nodes['l'])

    print "print all words to make sure they are all there: "
    print trie.get_all()

    print "print out all the words with the given prefixes: "
    print trie.get_all_with_prefix("g")
    print trie.get_all_with_prefix("go")
    print trie.get_all_with_prefix("co")
    print trie.get_all_with_prefix("hom")
    print trie.get_all_with_prefix("gr")


