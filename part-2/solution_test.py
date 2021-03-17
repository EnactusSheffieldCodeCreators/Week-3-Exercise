import solution

class TestClass:
    # testing extract_text function
    def test_extract_text(self):
        test_list = [{'text': 'hey', 'start': 3.28, 'duration': 6.239}, 
                    {'text': "uh if we got sound uh let's just check", 'start': 5.04, 'duration': 6.72}, 
                    {'text': 'uh', 'start': 9.519, 'duration': 2.241}, 
                    {'text': "okay uh let's look at that", 'start': 12.719, 'duration': 6.001}, 
                    {'text': 'um', 'start': 16.48, 'duration': 2.24}]
        extracted_list = solution.extract_text(test_list)
        expected_list = ['hey',
                        "uh if we got sound uh let's just check",
                        'uh',
                        "okay uh let's look at that",
                        'um']
        assert extracted_list == expected_list

    # testing ngrams function
    def test_ngrams(self):
        test_string = "hello this is nam"
        test_list = test_string.split(' ')

        expected_list = [('hello', 'this'), ('this', 'is'), ('is', 'nam')]
        expected_string = [('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o'), ('o', ' '), (' ', 't'), ('t', 'h'), ('h', 'i'), ('i', 's'), ('s', ' '), (' ', 'i'), ('i', 's'), ('s', ' '), (' ', 'n'), ('n', 'a'), ('a', 'm')]
        
        # This test is for bigrams ONLY, more tests need to be done for different number of grams 
        assert expected_list == solution.ngrams(test_list,2) and expected_string == solution.ngrams(test_string,2) 

    # testing extract_ngrams function
    def test_extract_ngrams(self):
        test_string = 'hello how are you'
        test_ngram_range = (1,2)

        expected_results = {('hello',): 1, ('how',): 1, ('are',): 1, ('you',): 1, ('hello', 'how'): 1, ('how', 'are'): 1, ('are', 'you'): 1}
        
        assert expected_results == solution.extract_ngrams(test_string,test_ngram_range)

    # testing get_top_common_phrase function
    def test_get_top_common_phrase(self):
        test_dict = {('hello',): 2, ('how',): 1, ('are',): 1, ('you',): 1, ('hello', 'how'): 1, ('how', 'are'): 1, ('are', 'you'): 1}
        test_key,test_value = solution.get_top_common_phrase(test_dict)
        assert test_key == ('hello',) and test_value == 2
