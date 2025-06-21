"""
Albanian language words processing module.

This module provides functionality to access and filter Albanian words
from a dataset, with options to include word types and definitions.
"""

import ast
import csv
import os
from typing import Dict, List, Optional, Set, Union

import pkg_resources


def get_all_words(
    starts_with: Optional[str] = None,
    includes: Optional[str] = None,
    return_type: bool = False,
    return_definition: bool = False,
) -> Union[List[str], List[Dict]]:
    """
    Get Albanian words filtered by optional criteria with additional information.

    This function reads words and their details from a CSV file and filters them
    based on provided criteria. It can also format the output to include word
    types and definitions.

    Args:
        starts_with: If provided, only words that start with this substring are returned.
        includes: If provided, only words that include this substring are returned.
        return_type: If True, includes the word type in the return data.
        return_definition: If True, includes the word definition in the return data.

    Returns:
        Depending on the parameters, returns either a list of words or a list of
        dictionaries with word details.

    Examples:
        >>> # Get all words
        >>> all_words = get_all_words()
        >>> # Get words starting with 'sh'
        >>> sh_words = get_all_words(starts_with='sh')
        >>> # Get words with definitions
        >>> words_with_def = get_all_words(return_definition=True)
    """
    words: List = []
    seen_words: Set[str] = set()

    try:
        filename = pkg_resources.resource_filename("albanianlanguage", "data/words.csv")

        with open(filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                word = row.get("word", "")

                # Apply filters if specified
                if (starts_with and not word.lower().startswith(starts_with.lower())) or (
                    includes and includes.lower() not in word.lower()
                )::
                    continue

                # Skip duplicate words
                if word in seen_words:
                    continue

                if return_type or return_definition:
                    word_details = {"word": word}

                    if return_type and "type" in row:
                        word_details["type"] = row["type"]

                    if return_definition and "definition" in row:
                        try:
                            word_details["definition"] = ast.literal_eval(
                                row["definition"]
                            )
                        except (SyntaxError, ValueError):
                            # Handle malformed definition data
                            word_details["definition"] = row["definition"]

                    words.append(word_details)
                else:
                    words.append(word)

                seen_words.add(word)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Albanian words data file not found. Check the package installation."
        )
    except Exception as e:
        raise RuntimeError(f"Error processing Albanian words data: {str(e)}")

    return words
