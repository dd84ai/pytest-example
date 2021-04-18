
"module to test any present urls"

import pytest
from test import current_app


@pytest.mark.asyncio
async def test_app():
    "checking that we can get main page"
    client = current_app.test_client()
    response = await client.get('/')
    assert (response.status_code == 200) or (response.status_code == 302)
