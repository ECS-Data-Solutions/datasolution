from starlite import Starlite, Provide
import uvicorn
from src.plugins import SQLA_PLUG

# Routers
from routes.v0 import router
# End Routers

app = Starlite(
    route_handlers=[
        router
    ],
    plugins=[
        SQLA_PLUG
    ],
)
for i in app.routes:
    print(i.path_components)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        log_level="debug",
        port=443,
        timeout_keep_alive=0,
    )
