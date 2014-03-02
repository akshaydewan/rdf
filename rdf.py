import nltk
from random import choice
from random import random

#Before past tense verb:
vbd = ["kind of", "smartly", "already"]
vbd_ignore = []
vbd_prob = 0.75
#Before past participle verb:
vbn = ["kind of", "smartly", "already"]
vbn_ignore = []
vbn_prob = 0.30
#Before gerund verb:
vbg = ["kind of", "smartly"]
vbg_ignore = []
vbg_prob = 0.6
#Before present tense verb:
vbp = ["smartly"]
vbp_ignore = ["are"]
vbp_prob = 0.75
#Before present tense 3rd person singular
vbz = ["smartly", "kind of"]
vbz_ignore = ["is", "'s"]
vbz_prob = 0.75
#Before superlative adjective
jjs = ["kind of"]
jjs_ignore = []
jjs_prob = 0.5
#Before noun
nn = ["smart", "fancy", "tremendous"]
nn_ignore = []
nn_prob = 0.30
#
#vbd_after = ["in production"]


def make_rdf(text):
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    index = 0
    fluff_list = []
    for t in pos_tags:
        pos = t[1]
        token = t[0]
        #print("Found POS: " + token + "->" + pos)
        fluff = ''
        if pos == "VBD":
            fluff = prepend_random(token, vbd, vbd_ignore, vbd_prob)
        elif pos == "VBG":
            fluff = prepend_random(token, vbg, vbg_ignore, vbg_prob)
        elif pos == "VBP":
            fluff = prepend_random(token, vbp, vbp_ignore, vbp_prob)
        elif pos == "VBZ":
            fluff = prepend_random(token, vbz, vbz_ignore, vbz_prob)
        elif pos == "JJS":
            fluff = prepend_random(token, jjs, jjs_ignore, jjs_prob)
        elif pos[:2] == "NN":
            fluff = prepend_random(token, nn, nn_ignore, nn_prob)
        if(len(fluff) > 0):
            fluff_list.append((fluff, index))
        index = index + 1
    return combine(fluff_list, tokens)  

#
# Chooses a random word based on the probability and ignore_list.
# Returns an empty string if no word is to be added
#
def prepend_random(token, word_list, ignore_list, probability):
        if token in ignore_list:
                return ''
        rand = random()
        if(0 <= rand <= probability):
                return choice(word_list)
        else:
                return ''

def combine(fluff_list, tokens):
        offset = 0
        for fluff in fluff_list:
                pos = fluff[1] + offset
                tokens.insert(pos, fluff[0])
                offset = offset + 1
        return ' '.join(tokens)

def main():
    print "Start"
    text = raw_input("Enter a string: ")
    print "===RDF form==="
    print make_rdf(text)
    
if __name__ == "__main__":main()    
