# Week-3-Exercise
Exercise for Week 3

# Code Walkthrough
We start by just print out the transcripts received from ```youtube_transcript_api``` and see what's inside, here's a sample of 3:

```
[{'text': 'hey', 'start': 3.28, 'duration': 6.239},
 {'text': "uh if we got sound uh let's just check", 'start': 5.04, 'duration': 6.72},
 {'text': 'uh', 'start': 9.519, 'duration': 2.241}]
```

So its a ***list of dicitonary***.

Since ```'start'``` and ```'duration'``` are probably not needed, we extract the ```'text'``` only into a list:

```
def extract_text(transcript):
    text_list = []
    for dictionary in transcript:
        text_list.append(dictionary['text'])
    return text_list
```

The method simply loop through the dictionary list and append the value of the ```text``` entry in each dictionary into a list. The same can be done using 1-line List Comprehension: ```text_list = [dictionary['text'] for dictionary in transcript]```.

## Extracting Phrases with N-grams
### A bit about N-gram

Considering this sentence:

```Javascript is the best language```

the n-gram with n = 2 will group 2 consecutive words, this is called ***bigram***. In the above example, it will return (Javascript, is), (is, the), (the,best), (best, language) for all possible bigrams. 

Phrases are essentially n-grams, depends on the length idk. This is why we need different n-grams.

### Extracting n-grams

Consecutive words can be obtained with a simple function:

```
def ngrams(t, n):
    g = []
    for i in range(len(t)-n+1):
        g.append(tuple(t[i:i+n]))
    return g
```

Here we loop through a sentence, at each index we append the n-gram tuple into a list and return it. Again if anyone fancy a 1-line method here's an alternative: ```g = [tuple(t[i:i+n]) for i in range(len(t)-n+1)]```.

But we need many n-grams (n=1, n=2, n=3, ...) and their count, that's why we need to repeat the process many times:

```
def extract_ngrams(text, ngram_range):
    ngram_dict = dict()
    for n in range(ngram_range[0],ngram_range[1]+1):
        tokens = text.lower().split(' ')
        ngrams_ = ngrams(tokens,n) 
        for ngram in ngrams_:
            if ngram in ngram_dict:
                ngram_dict[ngram] += 1
            else:
                ngram_dict[ngram] = 1
    return ngram_dict
```

The function first split the text into words (if not ```ngram``` will take consecutive characters instead of words). After extracting all n-grams into a list, we count each of them and store the occurences in a ```ngram_dict``` dictionary. The process is repeated for the range of n-gram provided (I designed so the parameter ngram_range is a list or tuple e.g (1,2) will take all unigram and bigram).

## Taking top frequent phrases

All the hard work is done basically. The last thing we do is to retrieve the most frequent phrase in the dictionary. Just loop through the dictionary and store the best result like so:

 ```
 def get_top_common_phrase(dictionary):
    top_key = []
    top_value = 0
    for key,value in dictionary.items():
        if value > top_value:
            top_value = value
            top_key = key

    return top_key, top_value
 ```
 
 Running the program should return the top phrase is: 
 
 ```
 The most common phrase is: 'uh you know' which occur 21 times
 ```

# Testing
Tests can be run with ```pytest -q solution_test.py```. There are 4 tests in total (since i made 4 functions). Usually you don't have to test every single function, it's better to test the ***action*** (have 1 testing function for ```get_water()``` instead of 2 for ```raised_arm()``` and ```grab_water_bottle()```).
