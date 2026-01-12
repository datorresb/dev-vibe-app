"""Tests for factorial function."""
import pytest
import sys
sys.path.insert(0, '/workspaces/dev-vibe-app/toy-example/src')

from calculator import factorial


def test_factorial_zero():
    """Factorial of 0 should be 1."""
    assert factorial(0) == 1


def test_factorial_one():
    """Factorial of 1 should be 1."""
    assert factorial(1) == 1


def test_factorial_five():
    """Factorial of 5 should be 120."""
    assert factorial(5) == 120


def test_factorial_negative():
    """Factorial of negative number should raise ValueError."""
    with pytest.raises(ValueError):
        factorial(-1)
