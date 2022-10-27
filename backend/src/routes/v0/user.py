from starlite import Controller, get
from src.models.User import User


class UserController(Controller):
    path = "/user"

    @get()
    def get_user_by_id(self, user_id: int) -> dict:
        user = User.query.filter_by(id=user_id).first()
        return {
            "id": user.id,
            "name": user.name,
            "fullname": user.fullname,
        }
