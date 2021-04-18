"""module to test if we have correctly loaded consts from files
or anywhere else"""
import pytest
import consts


@pytest.mark.asyncio
async def test_const_langs():
    "checking if we can get translator languages"
    assert len(consts.consts.belorus_langs) > 0

@pytest.mark.asyncio
async def test_const_words():
    "checking if we can get translator languages"
    assert len(consts.consts.query_testing_words) > 0
