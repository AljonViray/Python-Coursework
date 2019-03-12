# Submitter: dmishkan(Mishkanian, Daniel)
# Partner: asviray(Viray, Aljon)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
from goody import irange
import prompt
from random import choice


# For use in read_corpus: leave unchanged in this file
def word_at_a_time(file : open):
    for line in file:
        for item in line.strip().split():
                yield item


def read_corpus(os : int, file : open) -> {(str):[str]}:
    from collections import defaultdict
    words = word_at_a_time(file)
    
    word_list = [word for word in words]
    
    corpus = defaultdict(list)
    for i in range(len(word_list)-os):
        key = tuple(word_list[i+x] for x in range(os))
        if word_list[i+os] not in corpus[key]:
            corpus[key].append(word_list[i+os])

    corpus = dict(corpus.items())
    return corpus


def corpus_as_str(corpus : {(str):[str]}) -> str:
    string = ""
    for key in sorted(corpus.keys()):      
        string += '  ' + str(key) + ' can be followed by any of ' + str(corpus[key]) + '\n'
    
    v_list = list(corpus.values())
    len_list = []
    for i in range(0, len(v_list)):
        l = v_list[i]
        len_list.append(len(l))
    max_len = max(len_list)
    min_len = min(len_list)
    string += f'max/min list lengths = {max_len}/{min_len}\n'
    return string        


def produce_text(corpus : {(str):[str]}, start : [str], count : int) -> [str]:
    recent = start.copy()
    generated = start.copy()
    
    for i in range(count):
        try:
            gen_word = choice(corpus[tuple(recent)])
            recent.append(gen_word)
            recent.pop(0)
            generated.append(gen_word)
        except:
            generated.append(None)
            break
                        
    return generated



        
if __name__ == '__main__':
    # Write script here
    os = int(input('Choose the order statistic: '))
    if os < 0:
        raise Exception('os must be positive, try again.')
      
    file = input('Choose the file name to process: ')
    corpus = read_corpus(os, open(file))
    print(corpus_as_str(corpus))
      
    print(f'Choose {os} words to start with')
    words = []
    for i in range(os):
        words.append(input(f'Choose word {i+1}: '))
    count = int(input('Choose number of words for generation: '))
    if count < 0:
        raise Exception('count must be positive, try again.')
      
    print(produce_text(corpus, words, count))

              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
