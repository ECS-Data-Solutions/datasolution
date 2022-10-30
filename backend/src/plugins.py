from starlite.plugins.sql_alchemy import SQLAlchemyPlugin, SQLAlchemyConfig
import os
from starlite import DTOFactory

SQLA_CONF = SQLAlchemyConfig(
        connection_string=os.getenv("SQLA_KEY"), dependency_key="db_session"
    )

SQLA_PLUG = SQLAlchemyPlugin(
    config=SQLA_CONF
)

dto_factory = DTOFactory(plugins=[SQLA_PLUG])
