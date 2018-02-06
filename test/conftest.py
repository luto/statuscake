import pytest


@pytest.fixture
def statuscake():
    from . import testconfig
    import statuscake

    return statuscake.StatusCake(testconfig.api_key, testconfig.api_user)
