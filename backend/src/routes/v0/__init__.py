from starlite import Router

# Router Imports
from src.routes.v0.ping import PingController
from src.routes.v0.user import UserController
from src.routes.v0.table import TableController
# End Router Imports

__all__ = ["router"]

router = Router(
    path="/v0",
    route_handlers=[
        PingController,
        UserController,
        TableController,
    ]
)
