import pandas as pd

import sys
sys.path.append("..")  # TODO: Cheat to make src work

from src.constants import TO_DATA, CWE_TYPES
from src.read_chi_lines import readChiLines
from src.findFiles import findChiFiles

def linesToCsv(cwe_type:str):
    
    chi_files = findChiFiles(cwe_type)
        
    for file in chi_files:
        
        # initialize list of sentences
        rows = []
        
        # extract all lines from each CHAT file
        lines = readChiLines(file, cwe_type)
        
        for line in lines:
            rows.append({
                'child_id': line[0], # readChiLines() changes file to child_id (302 -> C302)
                'cwe_type': line[1], 
                'line_id': line[2],
                'line': line[3]})
        
        # convert list to pandas dataframe
        df_temp = pd.DataFrame(rows)
        df_temp.to_csv(f'{TO_DATA}cwe_lines/{line[0]}_{cwe_type}.csv', index=False, sep='\t')
        
    return print(f'Done with {cwe_type}')

for cwe_type in CWE_TYPES:
    linesToCsv(cwe_type)