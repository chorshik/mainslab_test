from typing import List, Optional

from app.db.repositories.base import BaseRepository
from app.models.bill import BillCreate, BillInDB

CREATE_BILL_QUERY = """
    INSERT INTO bills (client_name, client_org, number, sum, date, service)
    VALUES (:client_name, :client_org, :number, :sum, :date, :service)
    RETURNING id, client_name, client_org, number, sum, date, service;
"""

GET_ALL_BILLS_QUERY = f"""
    SELECT * FROM bills;
"""


class BillsRepository(BaseRepository):
	async def create_bill(self, *, new_bill: BillCreate) -> BillInDB:
		query_values = new_bill.dict()
		bill = await self.db.fetch_one(query=CREATE_BILL_QUERY, values=query_values)
		return BillInDB(**bill)

	async def get_all_bills(self, order_by: str | None = None,
	                        client_name: str | None = None,
	                        client_org: str | None = None) -> List[BillInDB]:
		if order_by:
			GET_ORDER_BILLS_QUERY = ""
			if order_by.find("-") == 0:
				GET_ORDER_BILLS_QUERY = f"""
				    SELECT * FROM bills
				    ORDER BY {order_by.removeprefix("-")} DESC ;"""
			elif order_by.find("+") == 0 or -1:
				GET_ORDER_BILLS_QUERY = f"""
				    SELECT * FROM bills
				    ORDER BY {order_by};"""

			bills_records = await self.db.fetch_all(
				query=GET_ORDER_BILLS_QUERY,
			)
			return [BillInDB(**l) for l in bills_records]

		if client_name:
			GET_ORDER_BILLS_QUERY = f"""SELECT * FROM bills WHERE client_name='{client_name}';"""
			bills_records = await self.db.fetch_all(
				query=GET_ORDER_BILLS_QUERY,
			)
			return [BillInDB(**l) for l in bills_records]

		if client_org:
			GET_ORDER_BILLS_QUERY = f"""SELECT * FROM bills WHERE client_org='{client_org}';"""
			print(GET_ORDER_BILLS_QUERY)
			bills_records = await self.db.fetch_all(
				query=GET_ORDER_BILLS_QUERY,
			)
			return [BillInDB(**l) for l in bills_records]

		bills_records = await self.db.fetch_all(
			query=GET_ALL_BILLS_QUERY,
		)
		return [BillInDB(**l) for l in bills_records]
