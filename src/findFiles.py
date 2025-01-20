# finds all files in given the folder name (i.e. desease type)

from constants import TO_POLER
import glob

def findChaFiles(desease_type:str) -> list:
    """finds all children ids in a folder

    Args:
        folder (str): name of folder in /data/POLER/ that contains the CHAT file

    Returns:
        list: list of children ids
    """
    list_of_cha_files = []
    for file in glob.glob(f"{TO_POLER}{desease_type}/*.cha"):
        file = file[-7:-4] # extract child id from file path
        list_of_cha_files.append(file) # append child id to list
    return list_of_cha_files

# TODO: I will turn all sentences into csv
def findCsvs(desease_type:str) -> list:
    """finds all csv children ids in a folder

    Args:
        folder (str): name of folder in /data/POLER/ that contains the CHAT file

    Returns:
        list: list of children csv fie names
    """
    all_csv_files = []
    #read all files
    for file in glob.glob(f"{TO_POLER}{desease_type}/*.csv"):
        file = file[-7:] # csv from file path
        all_csv_files.append(file) # append csv to list
    
    return all_csv_files
