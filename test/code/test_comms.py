
"unit tests to check daemon process, which communicates with monitoring"
import pytest
from test import current_app

from app.comms.messages import do_one_attempt

@pytest.mark.asyncio
async def test_check_registration_in_monitor():
    "checking if we can send data to monitoring"

    code = do_one_attempt(current_app)
    assert code == 200
