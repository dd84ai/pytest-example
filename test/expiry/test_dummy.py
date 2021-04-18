"module for tests which we don't wish to be made often"

import pytest
from test import current_app


@pytest.mark.asyncio
async def test_dummy():
    """first test in section, existing for pipline checker
    delete when real tests will appear"""
    assert True