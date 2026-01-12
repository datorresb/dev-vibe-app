"""Tests for the sqrt function."""
import pytest
import sys
sys.path.insert(0, '/workspaces/dev-vibe-app/toy-example/src')

from calculator import sqrt


def test_sqrt_basic():
    """Test basic square root calculations."""
    assert sqrt(4) == 2
    assert sqrt(9) == 3


def test_sqrt_zero():
    """Test square root of zero."""
    assert sqrt(0) == 0


def test_sqrt_negative_raises_error():
    """Test that square root of negative number raises ValueError."""
    with pytest.raises(ValueError):
        sqrt(-1)
