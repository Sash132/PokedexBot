"""This file holds a collection of tests that test most of the functions in the 
   Pokedex_Bot_Functions file. There is also an overarching function at the end of this 
   file that tests all of the test functions so that they will not need to be done 
   individually.
"""
from my_module.Pokedex_Bot_Functions import *

def test_get_number():
    """Runs three specific tests for the get_number function"""
    assert get_number("Pikachu") == 25
    assert get_number("Mew") == 151
    assert callable(get_number)
    
def test_get_type():
    """Runs three specific tests for the get_type function"""
    assert get_type("Pikachu") == "Electric"
    assert isinstance(get_type("Pikachu"),str)
    assert callable(get_type)
    
def test_get_stats():
    """Runs three specific tests for the get_stats function"""
    assert get_stats("Pikachu") == "HP: 35, Attack: 55, Defense: 40, Special Attack: 50, Special Defense: 50, Speed: 90"
    assert isinstance(get_stats("Pikachu"),str)
    assert callable(get_stats)

def test_get_BST():
    """Runs three specific tests for the get_BST function"""
    assert get_BST("Pikachu") == 320
    assert get_BST("Mew") == 600
    assert callable(get_BST)
    
def test_get_legendary_status():
    """Runs three specific tests for the get_legendary_status function"""
    assert get_legendary_status("Pikachu") == False
    assert isinstance(get_legendary_status("Pikachu"),bool)
    assert callable(get_legendary_status)
    
def test_get_height():
    """Runs three specific tests for the get_height function"""
    assert get_height("Pikachu") == "0.4 meters"
    assert isinstance(get_height("Pikachu"),str)
    assert callable(get_height)
    
def test_get_weight():
    """Runs three specific tests for the get_weight function"""
    assert get_weight("Pikachu") == "6.0 kilograms"
    assert isinstance(get_weight("Pikachu"),str)
    assert callable(get_weight)
    
def test_get_happiness():
    """Runs three specific tests for the get_happiness function"""
    assert get_happiness("Pikachu") == 70
    assert get_happiness("Mew") == 100
    assert callable(get_happiness)
    
def test_get_capture_rate():
    """Runs three specific tests for the get_capture_rate function"""
    assert get_capture_rate("Pikachu") == 190
    assert get_capture_rate("Mew") == 45
    assert callable(get_capture_rate)
    
def test_get_classification():
    """Runs three specific tests for the get_classification function"""
    assert get_classification("Pikachu") == "Mouse Pokemon"
    assert isinstance(get_classification("Pikachu"),str)
    assert callable(get_classification)
    
def test_get_abilities():
    """Runs three specific tests for the get_abilities function"""
    assert get_abilities("Pikachu") == "['Static', 'Lightningrod']"
    assert isinstance(get_abilities("Pikachu"),str)
    assert callable(get_abilities)
    
def test_check_quit():
    """Runs four specific tests for the check_quit function"""
    assert check_quit("Quit") == True
    assert check_quit("Word") == False
    assert isinstance(check_quit("Quit"),bool)
    assert callable(check_quit)
    
def test_check_other():
    """Runs four specific tests for the check_other function"""
    assert check_other("Other") == True
    assert check_other("Word") == False
    assert isinstance(check_other("Other"),bool)
    assert callable(check_other)
    
def test_is_pokemon():
    """Runs four specific tests for the is_pokemon function"""
    assert is_pokemon("Pikachu") == True
    assert is_pokemon("Chicken") == False
    assert isinstance(is_pokemon("Pikachu"),bool)
    assert callable(is_pokemon)
    
def test_is_info():
    """Runs four specific tests for the is_info function"""
    assert is_info("Number") == True
    assert is_info("Food") == False
    assert isinstance(is_info("Number"),bool)
    assert callable(is_info)
    
def test_text_matcher():
    """Runs three specific tests for the text_matcher function"""
    assert text_matcher("PiKaCHu") == "Pikachu"
    assert isinstance(text_matcher("PiKaCHu"),str)
    assert callable(text_matcher)
    
def test_all_functions():
    """Runs all of the test functions made in this file."""
    test_get_number()
    test_get_type()
    test_get_stats()
    test_get_BST()
    test_get_legendary_status()
    test_get_height()
    test_get_weight()
    test_get_happiness()
    test_get_capture_rate()
    test_get_classification()
    test_get_abilities()
    test_check_quit()
    test_check_other()
    test_is_pokemon()
    test_is_info()
    test_text_matcher()