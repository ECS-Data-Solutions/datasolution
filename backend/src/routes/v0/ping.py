from starlite import Controller, get


class PingController(Controller):
    path = "/ping"

    @get()
    def ping_message(self) -> dict:
        return {"message": "Pong!"}
