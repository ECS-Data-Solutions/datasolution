from starlite import Controller, get, post, delete, NotFoundException, Parameter
from src.models.Table import Table, CreateTableDTO
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


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
        result = await db_session.scalars(select(Table).where(Table.id == table_id))
        table = result.one_or_none()

        if table is None:
            raise NotFoundException("Table not found")

        return {
            "id": table.id,
            "name": table.name,
            "description": table.description,
            "cells": table.cells
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