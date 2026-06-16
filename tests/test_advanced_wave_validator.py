import pytest
import numpy as np
from AdvancedWaveValidator import AdvancedWaveValidator


class TestAdvancedWaveValidator:
    """Test suite for AdvancedWaveValidator class."""

    def test_initialization(self):
        """Test that the validator initializes with correct PHI value."""
        validator = AdvancedWaveValidator()
        assert validator.PHI == pytest.approx(1.6180339887)

    def test_harvest_jitter_returns_array(self):
        """Test that harvest_jitter returns a numpy array."""
        validator = AdvancedWaveValidator()
        result = validator.harvest_jitter(samples=100)
        assert isinstance(result, np.ndarray)

    def test_harvest_jitter_correct_length(self):
        """Test that harvest_jitter returns the correct number of samples."""
        validator = AdvancedWaveValidator()
        samples = 500
        result = validator.harvest_jitter(samples=samples)
        assert len(result) == samples

    def test_harvest_jitter_positive_values(self):
        """Test that harvest_jitter returns positive time deltas."""
        validator = AdvancedWaveValidator()
        result = validator.harvest_jitter(samples=100)
        assert np.all(result >= 0)

    def test_check_time_symmetry_runs(self, capsys):
        """Test that check_time_symmetry executes without error."""
        validator = AdvancedWaveValidator()
        validator.check_time_symmetry()
        captured = capsys.readouterr()
        assert "WHEELER-FEYNMAN" in captured.out
        assert "RESULTS" in captured.out

    def test_check_time_symmetry_output_contains_metrics(self, capsys):
        """Test that check_time_symmetry outputs required metrics."""
        validator = AdvancedWaveValidator()
        validator.check_time_symmetry()
        captured = capsys.readouterr()
        assert "Retarded Potential" in captured.out
        assert "Advanced Potential" in captured.out
        assert "Symmetry Ratio" in captured.out
        assert "STATUS" in captured.out
