from spellchecker import SpellChecker
import re
# f = open('./Term_Project/assets/eng-simple_wikipedia_2021_100K-sentences.txt', 'r')
# context = f.read()
# context_no_non_eng = re.sub("[^A-Za-z]", " ", context)
# context_nonEng_single_spcace = re.sub('\s+', ',', context_no_non_eng)
# clean_context = context_nonEng_single_spcace.lower()

# new = open("./Term_Project/assets/newdict.txt", 'w')
# new.write(clean_context)

spell = SpellChecker()
spell = spell.word_frequency.load_text_file("./Term_Project/assets/newdict.txt")

def correctspell(query):
    correct = spell.correction(query)
    return correct

def candidate(query):
    candidate = spell.candidates(query)
    return candidate