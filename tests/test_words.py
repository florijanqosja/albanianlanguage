"""Tests for the words module."""
import pytest
from unittest.mock import patch, mock_open
import os

from albanianlanguage import get_all_words


# Sample CSV data for testing
MOCK_CSV_DATA = """word,type,definition
shqipëri,noun,"['Albania', 'a country in southeastern Europe']"
jetë,noun,"['life']"
shkollë,noun,"['school', 'educational institution']"
shkoj,verb,"['to go', 'to walk']"
"""


@patch('albanianlanguage.words.pkg_resources.resource_filename')
@patch('builtins.open', new_callable=mock_open, read_data=MOCK_CSV_DATA)
def test_get_all_words_basic(mock_file, mock_resource):
    """Test getting all words without filters."""
    # Setup mock
    mock_resource.return_value = 'path/to/mock/words.csv'
    
    # Call function
    result = get_all_words()
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) == 4
    assert "shqipëri" in result
    assert "jetë" in result
    assert "shkollë" in result
    assert "shkoj" in result


@patch('albanianlanguage.words.pkg_resources.resource_filename')
@patch('builtins.open', new_callable=mock_open, read_data=MOCK_CSV_DATA)
def test_get_words_with_filter(mock_file, mock_resource):
    """Test filtering words."""
    # Setup mock
    mock_resource.return_value = 'path/to/mock/words.csv'
    
    # Test starts_with filter
    starts_result = get_all_words(starts_with="sh")
    assert len(starts_result) == 3
    assert "shqipëri" in starts_result
    assert "shkollë" in starts_result
    assert "shkoj" in starts_result
    assert "jetë" not in starts_result
    
    # Test includes filter
    includes_result = get_all_words(includes="j")
    assert len(includes_result) == 2
    assert "jetë" in includes_result
    assert "shkoj" in includes_result


@patch('albanianlanguage.words.pkg_resources.resource_filename')
@patch('builtins.open', new_callable=mock_open, read_data=MOCK_CSV_DATA)
def test_get_words_with_details(mock_file, mock_resource):
    """Test getting words with type and definition."""
    # Setup mock
    mock_resource.return_value = 'path/to/mock/words.csv'
    
    # Test with return_type and return_definition
    result = get_all_words(return_type=True, return_definition=True)
    
    assert isinstance(result, list)
    assert len(result) == 4
    
    # Check structure of returned items
    for item in result:
        assert isinstance(item, dict)
        assert "word" in item
        assert "type" in item
        assert "definition" in item
    
    # Check specific values
    shkolla = next(item for item in result if item["word"] == "shkollë")
    assert shkolla["type"] == "noun"
    assert "school" in shkolla["definition"] 