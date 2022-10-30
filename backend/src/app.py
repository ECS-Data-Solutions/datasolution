from starlite import Starlite, Provide
import uvicorn
from src.plugins import SQLA_PLUG, SQLA_CONF
from src.models import Base

# Routers
from routes.v0 import router
# End Routers


async def on_startup() -> None:
    """Initialize the database."""
    async with SQLA_CONF.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = Starlite(
    route_handlers=[
        router
    ],
    plugins=[
        SQLA_PLUG
    ],
    on_startup=[on_startup]
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
