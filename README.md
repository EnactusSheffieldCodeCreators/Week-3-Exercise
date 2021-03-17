# EXERCISES WEEK 3

## Continue with Jack's lecture transcript
This week exercise will go a bit further, you will need to create a few functions as well as testing them. Again just try to get as far as possible, don't worry if you couldn't finish it, there will be a detail walkthrough by mentors on Sunday (or you can Ping us on Discord). 

## Part 2 - Catchphrase!
The challenge is to work out what Jack's catchphrase for the lecture is. This means finding the phrase that he said the most through the entire lecture, there's many different ways to tackle this so see what result you get.

## Basic setup with ```youtube_transcript_api```
First install the library:

```
pip install youtube_transcript_api
```

Then in your Python solution file, import the library and retrieve lecture 2 transcript using its video ID:

```
from youtube_transcript_api import YouTubeTranscriptApi

VIDEO_ID = "alTRvtmWi7k"
video_transcript = YouTubeTranscriptApi.get_transcript(VIDEO_ID)
```

More detail about the API can be found [here](https://github.com/jdepoix/youtube-transcript-api). Have fun! 
