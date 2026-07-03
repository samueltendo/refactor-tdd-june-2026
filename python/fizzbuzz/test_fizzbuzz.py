from fizzbuzz import fizzbuzz 
import pytest

def test_returns_number_as_string():
    assert fizzbuzz(1) == "1"

def test_returns_fizz_for_multiples_of_3():
    assert fizzbuzz(3) == "Fizz"

def test_returns_buzz_for_multiples_of_5():
    assert fizzbuzz(5) == "Buzz"
    
def test_returns_7_for_7():
    assert fizzbuzz(7) != "Fizz"
    assert fizzbuzz(7) != "Buzz"
    # assertNotEquals(fizzbuzz(7), 'FizzBuzz')

def test_returns_fizzbuzz_for_multiples_of_15(): 
    assert fizzbuzz(15) == "FizzBuzz"

def test_returns_fizz_for_another_multiple_of_3():
    assert fizzbuzz(9) == "Fizz"
    
def test_function_only_allows_integers():
    with pytest.raises(TypeError):
        fizzbuzz(1.5)
        
def test_function_only_allows_integers():
    with pytest.raises(TypeError):
        fizzbuzz("Eve")
