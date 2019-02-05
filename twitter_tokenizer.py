from nltk.tokenize import TweetTokenizer
from nltk import word_tokenize
import io
from collections import Counter
import pickle


TOKENIZER_CACHE = "data/tokenizer_serialized.pkl"


def get_corpus(file="data/twittercorpus.txt"):
	with io.open(file, "r", encoding="utf8") as f:
		corpus = f.read()
	return corpus


def load_contractions(file="data/list_of_contractions.txt"):
	contractions = {}
	with open(file, "r") as f:
		for line in f.readlines():
			meaning = line.split(maxsplit=1)[1].split("/")[0]
			contractions[line.split()[0].lower()] = len(meaning.split())
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


def _save_token_object(tokens):
	with open(TOKENIZER_CACHE, "wb") as tok_file:
		pickle.dump(pickle.dumps(tokens), tok_file)


def _load_token_object():
	with open(TOKENIZER_CACHE, "rb") as tok_file:
		return pickle.loads(pickle.load(tok_file))


def nltk_tok(result_file="data/microblog2011_tokenized.txt", tokenizer_result="data/tokenizer_serialized.txt"):
	tokenizer = TweetTokenizer()
	corpus = get_corpus()
	contractions = load_contractions()
	with io.open(result_file, "w",
							 encoding="utf8") as f:
		with io.open("data/dif_tweettok_vs_tok.txt", "w", encoding="utf8") as dif:
			count = 0
			for msg in corpus.split("\n"):
				tweet_tok = tokenizer.tokenize(msg.lower())
				tweet_tok = _tokenize_contractions(tweet_tok, contractions)
				tok = word_tokenize(msg.lower())
				f.write('%s\n' % str.join(' ', tweet_tok))
				if len(tweet_tok) != len(tok):
					dif.write("tweet_tok:\t%s\nnltk_tok:\t%s\n" %
										(str.join(' ', tweet_tok), str.join(' ', tok)))
					dif.write("#################################\n")
		tokens = tokenizer.tokenize(corpus.lower())
		#f.write(str(Counter(tokens)))
		_save_token_object(tokens)	
	return tokens


def regular_tok():
	from nltk import word_tokenize

#######################
# b. Stats            #
#######################
##########################
# c. Tokens' frequencies #
##########################
def stats(tokens):
	count = Counter(tokens)
	one_occurencies = 0
	with io.open("data/Tokens.txt", "w", encoding="utf8") as tok:
		for token in count.most_common():
			tok.write("%s\t%s\n" % (str(token[0]), str(token[1])))
			if token[1] == 1:
				one_occurencies += 1
	total_tokens = sum(count.values())
	unique_tokens = len(set(tokens))
	""" The type/token ratio is defined as the number of types
	 divided by the number of tokens."""
	type_token_ration = unique_tokens / total_tokens
	with open("data/stats_b.txt", "w") as f:
		f.write("""Total tokens: %s\nUnique tokens: %s\nType/token ration: %s\n
						""" % (str(total_tokens), str(unique_tokens),
									 str(type_token_ration)))
		f.write("Number of tokens that appear only once: %s\n"
			   		% str(one_occurencies))


##########################
# e. words               #
##########################
# def extract words(tokens):





def main():
	load = input("Load cached tokens: ")
	if load == "y":
		tokens = _load_token_object()
	else:
		tokens = nltk_tok()

	stats(tokens)


main()
