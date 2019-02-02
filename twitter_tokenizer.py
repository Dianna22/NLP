from nltk.tokenize import TweetTokenizer
import io
from collections import Counter
import json

def get_corpus(file="twittercorpus.txt"):
	with io.open(file, "r", encoding="utf8") as f:
		corpus = f.read()
	return corpus

def nltk_tok(result_file="microblog2011_tokenized.txt"):
	tokenizer = TweetTokenizer()
	corpus = get_corpus()
	with io.open(result_file, "w",
							 encoding="utf8") as f:
		f.write("#################################\n")
		f.write("# First 20 sentences tokenized: #\n")
		f.write("#################################\n")
		for msg in corpus.split("\n")[:20]:
			f.write("%s\n" % str(tokenizer.tokenize(msg)))
		f.write("#################################\n")
		f.write("# Tokenizer report:             #\n")
		f.write("#################################\n")
		tokens = tokenizer.tokenize(corpus)
		f.write(str(Counter(tokens)))
		return tokens

nltk_tok()
