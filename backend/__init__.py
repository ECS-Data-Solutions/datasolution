from starlite import Starlite
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin, SQLAlchemyConfig
import os
from routes.v1 import router as v1_router

app = Starlite(
    route_handlers=[
        v1_router
    ],
    plugins=[
        SQLAlchemyPlugin(
            config=SQLAlchemyConfig(
                connection_string=os.getenv("SQLA_KEY"), dependency_key="async_session"
            )
        ),
    ],
)
