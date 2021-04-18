
"module to test anything related to serche engines"

import pytest
from test import current_app

from app.api.search.routes import info_search_find

@pytest.mark.asyncio
async def test_search_types():
    "checking json response from api/search/types api request"
    client = current_app.test_client()
    # ,json=json_data
    response = await client.get(f"/api/search/types?api={current_app.config['SECRET_KEY']}")
    data = await response.get_json(force=True)
    assert 'success' in data


@pytest.mark.asyncio
async def test_search_find():
    "checking json response to get from api/search/find api request"
    client = current_app.test_client()
    json_data = dict(info_search_find.data['input_min'])
    response = await client.get(
        f"/api/search/find?api={current_app.config['SECRET_KEY']}",
        json=json_data
        )
    data = await response.get_json(force=True)
    assert 'success' in data
