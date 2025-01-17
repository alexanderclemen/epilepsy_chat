# function to clean sentence from one unimportant symbol
import re

def removeDotString(sentence, regex = re.compile(r' \w{1,13}')):
     #  works but \\x15 does not
    sentence = re.sub(pattern = regex, repl = '', string = sentence)
    return sentence