from typing import Literal, Optional
from fastapi import FastAPI

from src.services.gateway import ServicesGateway
from src.api.common.mediator.mediator import CommandMediator
from src.services.factory import create_service_gateway_factory
from src.database.core import (
    create_engine,
    create_async_session_maker,
    TransactionManager,
)
from src.database.gateway import DBGateway
from src.core.settings import DatabaseSettings
from src.database.factory import create_database_factory
from src.common.tools import singleton


APP_STATUS = Literal["test", "production"]


def init_dependencies(
    app: FastAPI,
    db_settings: DatabaseSettings,
    app_status: Optional[APP_STATUS] = "production",
) -> None:
    engine = create_engine(
        db_settings.get_url_obj if app_status == "production" else db_settings.TEST_HOST
    )
    session = create_async_session_maker(engine)
    db_factory = create_database_factory(TransactionManager, session)
    service_factory = create_service_gateway_factory(db_factory)


    mediator = CommandMediator()
    mediator.setup(
        engine=engine,
        session=session,
        db_gateway=db_factory,
        service_gateway=service_factory,
        
    )


    app.dependency_overrides[CommandMediator] = singleton(mediator)
    app.dependency_overrides[ServicesGateway] = service_factory
    app.dependency_overrides[DBGateway] = db_factory