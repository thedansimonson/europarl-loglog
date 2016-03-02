import os
import nltk.corpus
import ft
import matplotlib.pyplot as plt
import numpy as np

europarl_path = "../../nltk_data/corpora/europarl_raw/"
path, langs, crap = os.walk(europarl_path).next()

lang_word_counts = {}
rank_counts = {}
for lang in langs:
    reader = nltk.corpus.EuroparlCorpusReader(europarl_path+lang, ".*")
    lang_word_counts[lang] = ft.histo(
                                ft.indexBy("word", 
                                    ft.singletons("word",
                                        [w for w in reader.words()])))
    rank_counts[lang] = sorted(lang_word_counts[lang].items(), key = lambda x: -x[1])

for lang in rank_counts:
    plt.loglog(range(1, len(rank_counts[lang])+1), 
             [c for w,c in rank_counts[lang]], label = lang)
plt.legend()
plt.show()




