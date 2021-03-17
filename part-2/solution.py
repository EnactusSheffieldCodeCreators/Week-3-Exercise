# Solution to part 2, Try to do it yourself first.

# ==== Imports =====
from youtube_transcript_api import YouTubeTranscriptApi # pip install youtube_transcript_api

# ===== Constants =====
VIDEO_ID = "alTRvtmWi7k"

# ===== Find jack's catchphrase ======
def extract_text(transcript):
    """
        data: raw transcript retrieved from YouTubeTranscriptApi
        return: list of text extracted from data
    """
    text_list = []
    for dictionary in transcript:
        text_list.append(dictionary['text'])
    
    # Using list comprehension: 
    # text_list = [dictionary['text'] for dictionary in transcript]
    return text_list
    
def ngrams(t, n):
    """
        Extract n-gram from a string to a list of tuples
        e.g. 2-gram example: "hello this is nam" -> [('hello', 'this'), ('this', 'is'), ('is', 'nam')]
    """
    g = []
    for i in range(len(t)-n+1):
        g.append(tuple(t[i:i+n]))
    return g

def extract_ngrams(text, ngram_range):
    """
        Count ngram for a range of n-grams
        return: dictionary containing n-grams and their count
    """
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

def get_top_common_phrase(dictionary):
    """
        dictionary: input a dictionary
        return: the top key by its count value (most frequent key)
    """
    top_key = []
    top_value = 0
    for key,value in dictionary.items():
        if value > top_value:
            top_value = value
            top_key = key

    return top_key, top_value

if __name__ == "__main__":
    # Get the transcript
    # Transcipt is a list of dictionaries, with entries: 'text', 'start', 'duration'
    ''' SAMPLE
    {'text': 'hey', 'start': 3.28, 'duration': 6.239}
    {'text': "uh if we got sound uh let's just check", 'start': 5.04, 'duration': 6.72}
    {'text': 'uh', 'start': 9.519, 'duration': 2.241}
    '''
    video_transcript = YouTubeTranscriptApi.get_transcript(VIDEO_ID)

    # Extracting the whole transcript text
    text_list = extract_text(video_transcript)
    transcript = ' '.join(text_list)

    # Count n-grams from the transcript text
    ngrams = extract_ngrams(transcript,(3,8))

    # Getting the most frequent phrase    
    k,v = get_top_common_phrase(ngrams)
    print("The most common phrase is: '{}' which occur {} times".format(' '.join(k),v)) # Print the phrase and its count

    # Here's another way to retrieve the top frequent keys
    #  - First sort it by the value
    #  - Then simply take the top 10
    #sorted_x = sorted(ngrams.items(), key=lambda kv: kv[1], reverse=True)
    #for i in sorted_x[:10]:
    #    print(i)
