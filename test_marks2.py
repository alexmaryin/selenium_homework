import pytest


class TestPage2:
    @pytest.mark.xfail(strict=True)
    def test_succeed(self):
        assert True

    @pytest.mark.xfail
    def test_not_succeed(self):
        assert False

    @pytest.mark.skip
    def test_skipped(self):
        assert False
