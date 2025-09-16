import pytest
import pydantic
from app.models import MsgPayload

def test_msg_payload_creation():
    payload = MsgPayload(msg_id=1, msg_name="traying")

    assert payload.msg_name == "traying"
    assert payload.msg_id == 1

def test_msg_payload_missing_required_field_correctly_fails():
    with pytest.raises(pydantic.ValidationError):
        MsgPayload()

def test_msg_payload_missing_name_fails():
    with pytest.raises(pydantic.ValidationError):
        MsgPayload(msg_id=1)