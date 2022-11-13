from sqlalchemy.orm import selectinload
from starlite import Controller, get, post, delete, NotFoundException, Parameter
from src.models.Table import Table, CreateTableDTO
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.Cell import Cell, CreateCellDTO


class TableController(Controller):
    path = "/table"

    @post()
    async def create_table(
            self,
            data: CreateTableDTO,
            db_session: AsyncSession
    ) -> dict:
        table = Table(**data.dict())
        db_session.add(table)
        await db_session.commit()
        return {
            "msg": "Table created successfully"
        }

    @get()
    async def get_table_by_id(
            self,
            table_id: int,
            db_session: AsyncSession
    ) -> dict:
        result = await db_session.scalars(select(Table).where(Table.id == table_id).options(selectinload(Table.cells)))
        table = result.one_or_none()

        if table is None:
            raise NotFoundException("Table not found")

        # serialize cells
        cells = []
        for cell in table.cells:
            cells.append({
                "id": cell.id,
                "locator": cell.locator,
                "description": cell.description,
                "value": cell.value,
            })

        return {
            "id": table.id,
            "name": table.name,
            "description": table.description,
            "cells": cells
        }

    @get("/list")
    async def get_table_list(
            self,
            db_session: AsyncSession
    ) -> list:
        result = await db_session.execute(select(Table))
        table_list_pre = result.scalars().all()
        table_list = []

        for i in table_list_pre:
            table_list.append({
                "id": i.id,
                "name": i.name,
                "description": i.description,
            })

        return table_list

    # cells

    @post("/cell")
    async def create_cell(
            self,
            data: CreateCellDTO,
            db_session: AsyncSession
    ) -> dict:
        data = data.dict()
        result = await db_session.scalars(select(Table).where(Table.id == data["table_id"]).options(selectinload(Table.cells)))
        table = result.one_or_none()

        if table is None:
            raise NotFoundException("Table not found")
        data.pop("table_id")
        data["table"] = table

        cell = Cell(**data)
        db_session.add(cell)
        await db_session.commit()
        return {
            "msg": "Cell created successfully"
        }
