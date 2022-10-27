from starlite import Starlite
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin, SQLAlchemyConfig
import os
import uvicorn

# Routers
from routes.v0 import router
# End Routers

app = Starlite(
    route_handlers=[
        router
    ],
    plugins=[
        SQLAlchemyPlugin(
            config=SQLAlchemyConfig(
                connection_string=os.getenv("SQLA_KEY"), dependency_key="async_session"
            )
        ),
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
