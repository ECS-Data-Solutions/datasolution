from sqlalchemy.orm import relationship
from src.models import Base, dto_factory
from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey
import datetime

__all__ = ["Cell"]

class Cell(Base):
    __tablename__ = "cells"
    id = Column(Integer, primary_key=True)
    locator = Column(String)
    description = Column(String)
    value = Column(String)
    table_id = Column(Integer, ForeignKey("tables.id"))

    def __repr__(self) -> dict:
        return {
            "id": self.id,
            "table_id": self.table_id,
            "description": self.description,
            "value": self.value,
        }


CreateCellDTO = dto_factory("CreateCellDTO", Cell, exclude=["id"])
