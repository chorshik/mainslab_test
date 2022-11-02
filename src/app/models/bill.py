from typing import Optional
from enum import Enum
from app.models.core import IDModelMixin, CoreModel


class ServiceType(str, Enum):
	pass


class BillBase(CoreModel):
	client_name: Optional[str]
	client_org: Optional[str]
	number: Optional[int]
	sum: Optional[float]
	date: Optional[str]
	service: Optional[str]


class BillCreate(BillBase):
	client_name: Optional[str]
	client_org: Optional[str]
	number: Optional[int]
	sum: Optional[float]
	date: Optional[str]
	service: Optional[str]


class BillInDB(IDModelMixin, BillBase):
	client_name: Optional[str]
	client_org: Optional[str]
	number: Optional[int]
	sum: Optional[float]
	date: Optional[str]
	service: Optional[str]


class BillPublic(IDModelMixin, BillBase):
	pass
