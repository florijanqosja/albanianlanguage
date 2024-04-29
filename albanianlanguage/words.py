import csv
import ast
import pkg_resources


def get_all_words(starts_with=None, includes=None, return_type=False, return_definition=False):
    """
    Reads words and their details from a CSV file and optionally filters them based on provided criteria. 
    Can also format the output to include word types and definitions.
    
    Parameters:
    filename (str): The path to the CSV file containing the words. Default is 'wordtype/ff.csv'.
    starts_with (str, optional): If provided, only words that start with this substring are returned.
    includes (str, optional): If provided, only words that include this substring are returned.
    return_type (bool, optional): If True, includes the word type in the return data.
    return_definition (bool, optional): If True, includes the word definition in the return data.
    
    Returns:
    list: Depending on the parameters, returns either a list of words or a list of dictionaries with word details.
    """
    words = []
    filename = pkg_resources.resource_filename('albanianlanguage', 'words.csv')

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word = row['word']
            # Check if the word meets the 'starts_with' or 'includes' condition
            if (starts_with and not word.startswith(starts_with)) or (includes and includes not in word):
                continue
            
            if return_type or return_definition:
                word_details = {'word': word}
                if return_type and 'type' in row:
                    word_details['type'] = row['type']
                if return_definition and 'definition' in row:
                    word_details['definition'] = ast.literal_eval(row['definition'])
                words.append(word_details)
            else:
                words.append(word)
    return words
