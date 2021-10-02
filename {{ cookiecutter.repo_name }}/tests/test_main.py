import pytest

class TestMain:
    def test_function_1(self):
        assert 1/3 == pytest.approx(0.33333333)
        assert len([1, 2, 3]) == 3
    
    def test_function_2(self):
        assert "A" in ["A", "B", "C"]
        assert 1 < 3
