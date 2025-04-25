
# predictors for the random forest classifier analysis
# you may comment those out that have the lowest feature importance
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