import json
from src.models.history_model import HistoryModel


# Req. 8
def test_request_history():
    test_obj = {
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt",
    }

    history = json.loads(HistoryModel.list_as_json())
    assert test_obj["text_to_translate"] == history[0]["text_to_translate"]
    assert test_obj["translate_from"] == history[0]["translate_from"]
    assert test_obj["translate_to"] == history[0]["translate_to"]
