# constants used in the project

# paths
TO_DATA = '../data/'
TO_POLER = '../data/POLER/'

# types of children
CWE_TYPES = ['Chronic', 'NewOnset', 'Match']

# CHAT Transcription annotation and their regular expressions
# taken from https://talkbank.org/manuals/CLAN.pdf
CHAT_SYMBOLS = {"repetition": r'\[\/\]', # A speaker begins to say something, stops and then repeats the earlier material without change.
                "retraction": r'\[\/\/\]', # a speaker starts to say something, stops, repeats the basic phrase, changes the syntax but maintains the same idea
                # e.g. *CHI: <the fish is> [//] the [/] the fish are swimming.
                "unfilled_pause": r'\(\.\)',
                "unfilled_pause_longer": r'\(\.\.\)',
                "unfilled_pause_longest": r'\(\.\.\.\)',
                "nonword": r'\(\&\~\)', # To avoid double counting, disfluencies that were contained within revisions were classified only as revisions.
                "filled_pause": r'\(\&\-\)', # e.g. "I want to go to the &-uh park"
                "error": r'\[\*\]' # THIS WOULD BE EXPLORATORY 
                }

PREDICTORS = ['repetition', 
              'retraction', 
              'unfilled_pause', 
              'unfilled_pause_longer', 
              'unfilled_pause_longest', 
            #   'nonword', # none exist
            #   'filled_pause', # none exist
              'error', 
              'nr_lines', 
              'nr_words', 
              'nr_words_per_line',
              'gender',
              'age_months'
              ]