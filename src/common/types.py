from typing import TypeVar

ModelType = TypeVar("ModelType", bound="Base")  # type: ignore # noqa: F821
ResultType = TypeVar("ResultType")
SessionFactory = TypeVar("SessionFactory")
GatewayType = TypeVar("GatewayType", bound="BaseGateway")  # type: ignore # noqa: F821
RepositoryType = TypeVar("RepositoryType")
DependencyType = TypeVar("DependencyType")