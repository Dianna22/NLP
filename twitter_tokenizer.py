from nltk.tokenize import TweetTokenizer
from nltk import word_tokenize
import io
from collections import Counter
import pickle
import re


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

def check_if_word(w_string):
	word = re.match("#?[a-zA-Z0-9]*[a-zA-Z][a-zA-Z0-9]*", w_string) 
	if word and word.group(0) == w_string:
		return word.group(0).replace("#", "")
	return None 


def extract_words(tokens):
	words = [check_if_word(token) for token in tokens if check_if_word(token) is not None]
	with io.open("data/words_frequency.txt", "w",
							 encoding="utf8") as f:
		count = Counter(words)
		for word in count.most_common():
			f.write("%s\t%s\n" % (word[0], str(word[1])))
	return words


def count_english_correct_words(words):
	from nltk.corpus import wordnet as wn
	counter = 0
	wrong_words = []
	for word in words:
		if wn.synsets(word):
			counter += 1
		else:
			wrong_words += [word]
	assert counter + len(wrong_words) == len(words)
	return (counter, wrong_words)


def _load_stopwords(file="data/list_of_Stopwords.txt"):
	with open(file, "r") as f:
		stopwords = f.read().split("\n")
	return stopwords


def eliminate_stopwords(words):
	stopwords = _load_stopwords()
	return [word for word in words if word not in stopwords]


def main():
	load = input("Rerun tokenizer: ")
	if load == "n":
		tokens = _load_token_object()
	else:
		tokens = nltk_tok()

	stats(tokens)
	words = extract_words(tokens)

	# correct_no_words, wrong_words = count_english_correct_words(words)

	print("e. Number of words: %s" % str(len(words)))
	# print("Number of recognized words: %s" % str(correct_no_words))
	print("Type/token ratio: %s" % str(len(set(words))/len(words)))

	words_no_stopwords = eliminate_stopwords(words)
	with io.open("data/words_frequency_no_stopwords.txt", "w",
							 encoding="utf8") as f:
		count = Counter(words_no_stopwords)
		for word in count.most_common():
			f.write("%s\t%s\n" % (word[0], str(word[1])))

if __name__=="__main__":
	main()
