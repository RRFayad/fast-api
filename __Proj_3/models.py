from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    hashed_password: Mapped[str] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True)
    role: Mapped[str] = mapped_column()
    phone_number: Mapped[str] = mapped_column()


class Todos(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # Primary key = Unique Identifier; Index = auto generate indexing
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    priority: Mapped[int] = mapped_column()
    complete: Mapped[bool] = mapped_column(default=False)
    owner: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
