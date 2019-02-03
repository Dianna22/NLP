from nltk.tokenize import TweetTokenizer
from nltk import word_tokenize
import io
from collections import Counter
import json


def get_corpus(file="data/twittercorpus.txt"):
	with io.open(file, "r", encoding="utf8") as f:
		corpus = f.read()
	return corpus


def load_contractions(file="data/list_of_contractions.txt"):
	contractions = {}
	with open(file, "r") as f:
		for line in f.readlines():
			meaning = line.split(maxsplit=1)[1].split("/")[0]
			contractions[line.split()[0]] = len(meaning.split())
	return contractions


#######################
# a. Tokenizer        #
#######################

def _insert_space_before_char(word, char):
	apostrophe = word.find(char)
	return "%s %s" % (word[:apostrophe],
										word[apostrophe:])


def _tokenize_contractions(words, contractions):
	for index in range(len(words)):
		if words[index] in contractions:
			words = words[:index] + word_tokenize(words[index]) + words[index+1:]
			# words[index] = _insert_space_before_char(words[index],"'")
	return words


def nltk_tok(result_file="data/microblog2011_tokenized.txt"):
	tokenizer = TweetTokenizer()
	corpus = get_corpus()
	contractions = load_contractions()
	with io.open("data/tokenize_first_20.txt", "w", encoding="utf8") as first_20:
		with io.open(result_file, "w",
								 encoding="utf8") as f:
			with io.open("data/dif_tweettok_vs_tok.txt", "w", encoding="utf8") as dif:	
				count = 0
				for msg in corpus.split("\n"):
					tweet_tok = tokenizer.tokenize(msg.lower())
					tweet_tok = _tokenize_contractions(tweet_tok, contractions)
					tok = word_tokenize(msg.lower())
					if count < 20:
						first_20.write('%s\n' % str.join(' ', tweet_tok))
					f.write('%s\n' % str.join(' ', tweet_tok))
					if len(tweet_tok) != len(tok):
						dif.write("tweet_tok:\t%s\nnltk_tok:\t%s\n" %
											(str.join(' ', tweet_tok), str.join(' ', tok)))
						dif.write("#################################\n")

			tokens = tokenizer.tokenize(corpus.lower())
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
	with open("data/stats_b.txt", "w") as f:
		f.write("""Total tokens: %s\nUnique tokens: %s\nType/token ration: %s
						""" % (str(total_tokens), str(unique_tokens),
									 str(type_token_ration)))

stats(tokens)

###
