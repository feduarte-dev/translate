from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    user = UserModel({"name": "Teste", "level": "admin", "token": "99999999"})
    user.save()

    history = [
        {
            "text-to-translate": "Hello, I like videogame",
            "translate-from": "en",
            "translate-to": "pt",
        },
        {
            "text-to-translate": "Do you love music?",
            "translate-from": "en",
            "translate-to": "pt",
        },
    ]

    for item in history:
        item["user-id"] = user.id
        HistoryModel(item).save()

    check_history = HistoryModel.find_one(
        {
            "text-to-translate": "Hello, I like videogame",
        }
    )

    check_user = UserModel.find_one({"name": "Teste"})

    app_test.delete(
        f"/admin/history/{check_history.data['_id']}",
        headers={"Authorization": f"Bearer {check_user.data['token']}"},
    )
