from nltk.tokenize import TweetTokenizer
import io
from collections import Counter
import json
#######################
# a. Tokenizer        #
#######################
def get_corpus(file="twittercorpus.txt"):
	with io.open(file, "r", encoding="utf8") as f:
		corpus = f.read()
	return corpus

def nltk_tok(result_file="microblog2011_tokenized.txt"):
	tokenizer = TweetTokenizer()
	corpus = get_corpus()
	with io.open(result_file, "w",
							 encoding="utf8") as f:
		# f.write("#################################\n")
		# f.write("# First 20 sentences tokenized: #\n")
		# f.write("#################################\n")
		f.write("#################################\n")
		f.write("# Tokenizer result:             #\n")
		f.write("#################################\n")		
		for msg in corpus.split("\n"):
			f.write('%s\n' %str.join(' ', tokenizer.tokenize(msg)))

		tokens = tokenizer.tokenize(corpus)
		#f.write(str(Counter(tokens)))
	return tokens

tokens = nltk_tok()

def regular_tok():
	from nltk import word_tokenize

#######################
# b. Stats            #
#######################
def stats(tokens):
	count = Counter(tokens)
	total_tokens = sum(count.values())
	unique_tokens = len(set(tokens))
	""" The type/token ratio is defined as the number of types
	 divided by the number of tokens."""
	type_token_ration = unique_tokens / total_tokens
	with open("stats_b.txt", "w") as f:
		f.write("""Total tokens: %s\nUnique tokens: %s\nType/token ration: %s
						""" % (str(total_tokens), str(unique_tokens),
									 str(type_token_ration)))

stats(tokens)
