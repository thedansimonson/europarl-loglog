# europarl-loglog
The [Europarl Corpus](http://www.statmt.org/europarl/) is a parallel corpus of transcripts from the European Parliament used for machine translation. This demo uses the corpus for showing the consistency of [Zipf's Law](https://en.wikipedia.org/wiki/Zipf%27s_law) across natural languages.

## What you need
* matplotlib
* nltk (uses the corpus reader)
* ft (library for manipulating lists of dictionaries: sudo pip install ft)

## Notes
You can get the corpus with nltk.download.

The path is hard-coded. You'll need to edit the europarl_path variable to the corpus location.
