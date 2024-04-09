# import gensim
# import gensim.downloader as api
# from gensim.models import Word2Vec
# from nltk.tokenize import sent_tokenize, word_tokenize
# import random
# import numpy as np


# class IncorrectAnswerGenerator:
#     def __init__(self, document):
#         self.model = api.load("glove-wiki-gigaword-100")
#         self.all_words = []
#         for sent in sent_tokenize(document):
#             self.all_words.extend(word_tokenize(sent))
#         self.all_words = list(set(self.all_words))

#     def get_all_options_dict(self, answer, num_options):
#         options_dict = dict()
#         try:
#             similar_words = self.model.similar_by_word(answer, topn=15)[::-1]

#             for i in range(1, num_options + 1):
#                 options_dict[i] = similar_words[i - 1][0]

#         except BaseException:
#             self.all_sim = []
#             for word in self.all_words:
#                 if word not in answer:
#                     try:
#                         self.all_sim.append((self.model.similarity(answer, word), word))
#                     except BaseException:
#                         self.all_sim.append((0.0, word))
#                 else:
#                     self.all_sim.append((-1.0, word))

#             self.all_sim.sort(reverse=True)

#             for i in range(1, num_options + 1):
#                 options_dict[i] = self.all_sim[i - 1][1]

#         replacement_idx = random.randint(1, num_options)

#         options_dict[replacement_idx] = answer

#         return options_dict

# import gensim.downloader as api
# from nltk.tokenize import word_tokenize
# import random
# from nltk.corpus import stopwords

# class IncorrectAnswerGenerator:
#     def __init__(self, document):
#         self.model = api.load("glove-wiki-gigaword-100")
#         self.all_words = set(word_tokenize(document.lower()))
#         self.stopwords = set(stopwords.words('english'))

#     def get_similar_word(self, word):
#         try:
#             similar_words = self.model.most_similar(word, topn=30)
#             similar_words = [w[0] for w in similar_words if w[0] not in self.stopwords and w[0] != word]
#             return random.choice(similar_words)
#         except KeyError:
#             return None

#     def get_all_options_dict(self, answer, num_options):
#         options_dict = dict()
#         similar_word = self.get_similar_word(answer)

#         if similar_word:
#             options_dict[1] = similar_word
#         else:
#             options_dict[1] = random.choice(list(self.all_words))

#         for i in range(2, num_options + 1):
#             options_dict[i] = random.choice(list(self.all_words - set(options_dict.values())))

#         replacement_idx = random.randint(1, num_options)
#         options_dict[replacement_idx] = answer

#         return options_dict

# import gensim.downloader as api
# from nltk.tokenize import word_tokenize
# import random
# from nltk.corpus import stopwords

# class IncorrectAnswerGenerator:
#     def __init__(self, document, output_file):
#         self.model = api.load("glove-wiki-gigaword-100")
#         self.all_words = set(word_tokenize(document.lower()))
#         self.stopwords = set(stopwords.words('english'))
#         self.output_file = output_file

#     def get_similar_word(self, word):
#         try:
#             similar_words = self.model.most_similar(word, topn=30)
#             similar_words = [w[0] for w in similar_words if w[0] not in self.stopwords and w[0] != word]
#             return random.choice(similar_words)
#         except KeyError:
#             return None

#     def get_all_options_dict(self, answer, num_options):
#         options_dict = dict()
#         similar_word = self.get_similar_word(answer)

#         if similar_word:
#             options_dict[1] = similar_word
#         else:
#             options_dict[1] = random.choice(list(self.all_words))

#         for i in range(2, num_options + 1):
#             options_dict[i] = random.choice(list(self.all_words - set(options_dict.values())))

#         replacement_idx = random.randint(1, num_options)
#         options_dict[replacement_idx] = answer

#         # Write options to the output file
#         with open(self.output_file, 'a') as f:
#             f.write(f"{options_dict}\n")

#         return options_dict

# import gensim.downloader as api
# from nltk.tokenize import word_tokenize
# import random
# from nltk.corpus import stopwords

# class IncorrectAnswerGenerator:
#     output_file = "incorrect_answers.txt"  # Define the output file as a class variable

#     def __init__(self, document):
#         self.model = api.load("glove-wiki-gigaword-100")
#         self.all_words = set(word_tokenize(document.lower()))
#         self.stopwords = set(stopwords.words('english'))

#     def get_similar_word(self, word):
#         try:
#             similar_words = self.model.most_similar(word, topn=50)
#             print(similar_words)
#             similar_words = [w[0] for w in similar_words if w[0] not in self.stopwords and w[0] != word]
#             return random.choice(similar_words)
#         except KeyError:
#             return None

#     def get_all_options_dict(self, answer, num_options):
#         options_dict = dict()
#         similar_word = self.get_similar_word(answer)

#         if similar_word:
#             options_dict[1] = similar_word
#         else:
#             options_dict[1] = random.choice(list(self.all_words))

#         for i in range(2, num_options + 1):
#             options_dict[i] = random.choice(list(self.all_words - set(options_dict.values())))

#         replacement_idx = random.randint(1, num_options)
#         options_dict[replacement_idx] = answer

#         # Write options to the output file
#         with open(self.output_file, 'a') as f:
#             f.write(f"{options_dict}\n")

#         return options_dict
import gensim.downloader as api
from nltk.tokenize import word_tokenize
import random
from nltk.corpus import stopwords
import string  # Import string module to handle punctuation

class IncorrectAnswerGenerator:
    output_file = "incorrect_answers.txt"  # Define the output file as a class variable

    def __init__(self, document):
        self.model = api.load("glove-wiki-gigaword-100")
        self.all_words = set(word_tokenize(document.lower()))
        self.stopwords = set(stopwords.words('english'))
        self.punctuation = set(string.punctuation)

    def get_similar_word(self, word):
        try:
            similar_words = self.model.most_similar(word, topn=50)
            similar_words = [w[0] for w in similar_words if w[0] not in self.stopwords and w[0] != word and not any(char in self.punctuation for char in w[0])]
            return random.choice(similar_words)
        except KeyError:
            return None

    def get_all_options_dict(self, answer, num_options):
        options_dict = dict()
        similar_word = self.get_similar_word(answer)

        if similar_word:
            options_dict[1] = similar_word
        else:
            options_dict[1] = random.choice([word for word in self.all_words if not any(char in self.punctuation for char in word)])

        for i in range(2, num_options + 1):
            options_dict[i] = random.choice([word for word in (self.all_words - set(options_dict.values())) if not any(char in self.punctuation for char in word)])

        replacement_idx = random.randint(1, num_options)
        options_dict[replacement_idx] = answer

        # Write options to the output file
        with open(self.output_file, 'a') as f:
            f.write(f"{options_dict}\n")

        return options_dict
