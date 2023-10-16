import pytest
from core.utils import get_chrome

@pytest.fixture(scope='session')
def browser():
    driver = get_chrome()
    yield driver
    driver.quit()

