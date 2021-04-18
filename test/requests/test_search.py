"module for tests which we don't wish to be made often"

import pytest
from test import current_app

from app.api.search.routes import info_search_find


@pytest.mark.asyncio
async def test_search_real_find():
    "checking..."
    client = current_app.test_client()

    # redacted code

    response = await client.get(
        f"/api/search?api={current_app.config['SECRET_KEY']}",
        json=json_data
        )
    data = await response.get_json(force=True)
    assert 'success' in data
    assert 'general' in data
    assert len(data['general']) > 0
    
    # redacted code
    
    assert count_translated > 0