# finds all files in given the folder name (i.e. desease type)

# I don't know why but i need to add src. even though they are in the same folder
from src.constants import TO_POLER, TO_DATA
import glob

def findChiFiles(cwe_type:str) -> list:
    """finds all children ids in a folder

    Args:
        cwe_type (str): name of folder in /data/POLER/ that contains the CHAT file

    Returns:
        list_of_cha_files (list): list of children ids
    """
    list_of_cha_files = []
    for file in glob.glob(f"{TO_POLER}{cwe_type}/*.cha"):
        file = file[-7:-4] # extract child id from file path
        list_of_cha_files.append(file) # append child id to list
    return list_of_cha_files

def findCsvs() -> list:
    """finds all csv children ids in a folder

    Returns:
        all_csv_files: list of children csv file names
    """
    all_csv_files = []
    #read all files
    for file in glob.glob(f"{TO_DATA}cwe_lines/*.csv"):
        # file = file[18:22] # csv from file path
        all_csv_files.append(file) # append csv to list
    
    return all_csv_files
