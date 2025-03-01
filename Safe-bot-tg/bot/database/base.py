from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from utils import camel_case_to_snake


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{camel_case_to_snake(cls.__name__)}s'

    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        fields = [f"{key}={repr(value)}" for key, value in self.__dict__.items() if not key.startswith('_')]
        return f"<{self.__class__.__name__}({', '.join(fields)})>"