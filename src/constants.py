# constants used in the project

# paths
TO_DATA = '../data/'
TO_POLER = '../data/POLER/'

# types of children
CWE_TYPES = ['Chronic', 'NewOnset', 'Match']

# CHAT Transcription annotation and their regular expressions
# taken from https://talkbank.org/manuals/CLAN.pdf
CHAT_SYMBOLS = {"repetition": r'\[\/\]', # A speaker begins to say something, stops and then repeats the earlier material without change.
                "retraction": r'\[\/\/\]' , # a speaker starts to say something, stops, repeats the basic phrase, changes the syntax but maintains the same idea
                # e.g. *CHI: <the fish is> [//] the [/] the fish are swimming.
                "unfilled_pause": r'\(\.\)',
                "unfilled_pause_longer": r'\(\.\.\)',
                "unfilled_pause_longest": r'\(\.\.\.\)',
                "nonword": r'&~\w+', 
                "filled_pause": r'&-\w+', # e.g. "I want to go to the &-uh park"
                "error": r'\[\*\]' # This is exploratory and is not in the original analysis
                }

# all predictors/features in the present analysis
PREDICTORS = ['repetition', 
              'retraction', 
              'unfilled_pause', 
              'unfilled_pause_longer', 
              'unfilled_pause_longest', 
              'nonword',
              'filled_pause', 
              'error', 
              'nr_lines', 
              'nr_words', 
              'nr_words_per_line',
              'gender',
              'age_months'
              ]

# these are removed during the random forest classifier analysis
predictors = [
              'repetition', # not in cwe_redent only
             'retraction', # not in cwe_chonic only
              'unfilled_pause',
              'nonword',
              'filled_pause',
              'error', 
              'nr_lines',
              'nr_words_per_line',
              'gender',
              'age_months'
              ]