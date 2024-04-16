from flask import Blueprint
from models.history_model import HistoryModel

history_controller = Blueprint("history", __name__)


@history_controller.route("/")
def get_history():
    return HistoryModel.list_as_json(), 200
