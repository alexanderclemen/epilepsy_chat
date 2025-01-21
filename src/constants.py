# constants used in the project

# paths
TO_DATA = '../data/'
TO_POLER = '../data/POLER/'

CWE_TYPES = ['Chronic', 'NewOnset', 'Match']

# taken from https://talkbank.org/manuals/CLAN.pdf
CHAT_SYMBOLS = {"repetition": r'\[\/\]',
                "retraction": r'\[\/\/\]',
                "unfilled_pause": r'\(\.\)',
                "unfilled_pause_longer": r'\(\.\.\)',
                "unfilled_pause_longest": r'\(\.\.\.\)',
                "nonword": r'\(\&\~\)', # To avoid double counting, disfluencies that were contained within revisions were classified only as revisions.
                "filled_pause": r'\(\&\-\)', # e.g. "I want to go to the &-uh park"
                "error": r'\[\*\]' # THIS WOULD BE EXPLORATORY 
                }