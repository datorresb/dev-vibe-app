"""Tests for the power function."""
import pytest
import sys
sys.path.insert(0, '/workspaces/dev-vibe-app/toy-example/src')

from calculator import power


def test_basic_power_operations():
    """Test basic power operations."""
    assert power(2, 3) == 8
    assert power(10, 0) == 1
    assert power(5, 1) == 5
    assert power(3, 2) == 9


def test_negative_exponents():
    """Test power with negative exponents."""
    assert power(2, -1) == 0.5
    assert power(4, -1) == 0.25
    assert power(10, -2) == 0.01


def test_fractional_exponents():
    """Test power with fractional exponents."""
    assert power(4, 0.5) == 2
    assert power(9, 0.5) == 3
    assert power(8, 1/3) == pytest.approx(2, rel=1e-9)
    assert power(27, 1/3) == pytest.approx(3, rel=1e-9)
