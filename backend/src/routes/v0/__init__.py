from starlite import Router

# Router Imports
from .ping import PingController
from .user import UserController
# End Router Imports

__all__ = ["router"]

router = Router(
    path="/v0",
    route_handlers=[
        PingController,
        UserController
    ]
)
