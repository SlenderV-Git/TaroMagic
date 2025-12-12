from src.services.user import UserService
from src.services.account import AccountService
from src.common.interfaces.gateway import BaseGateway
from src.database.gateway import DBGateway


class ServicesGateway(BaseGateway):
    __slots__ = "_database"

    def __init__(self, database: DBGateway) -> None:
        self._database = database
        super().__init__(database)

    def user(self) -> UserService:
        return UserService(repository=self._database.user())
    
    def account(self) -> AccountService:
        return AccountService(repository=self._database.account())
    
    #def name(self) -> NameService:
    #    return NameService(repository=self._database.name())