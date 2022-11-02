from typing import Callable, Type
from databases import Database
from fastapi import Depends
from starlette.requests import Request
from app.db.repositories.base import BaseRepository


def get_database(request: Request) -> Database:
	return request.app.state._db


def get_repository(repo_type: BaseRepository) -> Callable:
	def get_repo(db: Database = Depends(get_database)) -> BaseRepository:
		return repo_type(db)

	return get_repo
