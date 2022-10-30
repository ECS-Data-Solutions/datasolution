from starlite.plugins.sql_alchemy import SQLAlchemyPlugin, SQLAlchemyConfig
import os
from starlite import DTOFactory

SQLA_PLUG = SQLAlchemyPlugin(
    config=SQLAlchemyConfig(
        connection_string=os.getenv("SQLA_KEY"), dependency_key="db_session"
    )
)

dto_factory = DTOFactory(plugins=[SQLA_PLUG])
