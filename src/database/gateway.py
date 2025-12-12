from typing import Type
from src.database.repositories.account import AccountRepository
from src.database.repositories.user import UserRepository
from src.common.interfaces.gateway import BaseGateway
from src.common.types import RepositoryType
from src.database.core.manager import TransactionManager


class DBGateway(BaseGateway):
    def __init__(self, manager: TransactionManager) -> None:
        self.manager = manager
        super().__init__(manager)

    
    def user(self):
        return self._init_repo(UserRepository)
    
    def account(self):
        return self._init_repo(AccountRepository)


    '''def account(self):
        return self._init_repo(AccountRepository)'''

    
    def _init_repo(self, cls: Type[RepositoryType]) -> RepositoryType:
        return cls(self.manager.session)