# Epilepsy CHAT
This student project aims to reanalyse CHAT-annotated data of Children with Epilepsy from the [CHILDES Clinical English POLER Corpus][https://childes.talkbank.org/access/Clinical-Eng/POLER.html] with more advanced methods.

## Data
The data is publicly available https://git.talkbank.org/childes/data/Clinical-Eng/POLER.zip but one needs to be a registered user of https://childes.talkbank.org/

Raw data is read, cleaned, and written into ....cdv 

### variables
child_id: ID of the child (C302, C302, ..., )
cwe_type: Type of Chindren with Epilepsy (Chronic (n = 16), NewOnset (n = 10), Match (n = 26))

## Methods
- [x] from .cha files to .csv -> init_data.py
- [x] preprocessing:
  - [x] extract speech errors made by children -> preprocessing_errors_and_words.py
  - [x] add metadata to the data -> preprocessing_add_metadata.py
- [x] correlation analysis
- [x] remove correlated features 


## Preprocessing
1. `init_data.py`
2. `preprocessing_errors_and_words.py`
3. `preprocessing_add_metadata.py`
4. `rf_pipeline.py`
5. `correlation_matrix.R`
6. `preprocessing_rm_cor_feat.py`
7. `logistic_regression.R`