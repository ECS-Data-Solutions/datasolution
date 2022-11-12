from sqlalchemy.orm import relationship
from src.models import Base, dto_factory
from sqlalchemy import Column, Float, Integer, String, DateTime
from src.models.Cell import Cell

__all__ = ["Table"]

class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    cells = relationship("Cell", backref="table")

    def __repr__(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "cells": self.cells,
        }

CreateTableDTO = dto_factory("CreateTableDTO", Table, exclude=["id", "cells"])