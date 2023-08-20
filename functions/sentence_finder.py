from itertools import product

def find_real_sentences(string_of_letters: str, valid_word_list: list):
    """
    Function that returns a list of all valid sentences
    in a given string of letters (same order as the string)
    as per list of valid words.
    
    For example for:
        given input variables:
            string_of_letters = 'hereisnowapidocklands'
            valid_word_list = ['here', 'is', 'i', 'now', 'snow',
                 'api', 'pi', 'a', 'her',
                 'he', 'no', 'dock', 'lands', 'land',
                 'docklands', 'and']
        returns:
            ['here i snow a pi dock lands', 
            'here i snow a pi docklands', 
            'here i snow api dock lands', 
            'here i snow api docklands', 
            'here is now a pi dock lands', 
            'here is now a pi docklands', 
            'here is now api dock lands', 
            'here is now api docklands']
    
    """
    
    n = len(string_of_letters)

    loc_words = {i:[] for i in range(n)}

    for i in range(n):
        for y in range(i+1, n+1):
            potential_word = string_of_letters[i:y]
            if potential_word in valid_word_list:
                loc_words[i].append(potential_word)

    string_combinations = list(product(*[ls if len(ls) > 0 else [''] for ls in list(loc_words.values())]))

    real_sentences = []
    for s_i, s in enumerate(string_combinations):
        list_s = list(s)
        next_word_start = 0
        for i, char in enumerate(list_s):
            if i < next_word_start:
                list_s[i] = ''
            else:
                char_size = len(char)
                next_word_start = i + char_size
        if ('').join(list_s) == string_of_letters:
            real_sentence = (' ').join([x for x in list_s if x != ''])
            if real_sentence not in real_sentences:
                real_sentences.append(real_sentence)

    return real_sentences
