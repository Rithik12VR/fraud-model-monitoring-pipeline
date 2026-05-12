import pytest

from src.psi import bucket_score, calculate_psi


def test_calculate_psi_returns_zero_for_same_distribution():
    assert calculate_psi([10, 20, 30], [10, 20, 30]) == 0.0


def test_calculate_psi_returns_positive_for_different_distribution():
    assert calculate_psi([10, 20, 30], [30, 20, 10]) > 0


def test_calculate_psi_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        calculate_psi([10, 20], [10, 20, 30])


def test_bucket_score():
    bins = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    assert bucket_score(0.15, bins) == "0.0-0.2"
    assert bucket_score(0.99, bins) == "0.8-1.0"
