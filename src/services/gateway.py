from src.common.interfaces.gateway import BaseGateway
from src.database.gateway import DBGateway


class ServicesGateway(BaseGateway):
    __slots__ = "_database"

    def __init__(self, database: DBGateway) -> None:
        self._database = database
        super().__init__(database)

    #def name(self) -> NameService:
    #    return NameService(repository=self._database.name())