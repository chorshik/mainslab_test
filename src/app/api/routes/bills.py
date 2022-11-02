from typing import List, Optional
from io import StringIO
from datetime import datetime
import logging
from fastapi import APIRouter, File, UploadFile, Body, Depends, Header
from starlette.status import HTTP_201_CREATED
import pandas as pd
import numpy


from app.models.bill import BillCreate, BillPublic, BillInDB
from app.db.repositories.bills import BillsRepository
from app.api.dependencies.database import get_repository

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/uploadfile", name="bills:create-bill", status_code=HTTP_201_CREATED)
async def upload_csv(file: UploadFile = File(...),
                     bills_repo: BillsRepository = Depends(get_repository(BillsRepository))):
	format_ddmmyyyy = "%d.%m.%Y"
	try:
		data = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')
		for ind in data.index:
			if data['sum'][ind].replace('.', '').isdigit() and \
					data['service'][ind] is not ("" or "-") and \
					bool(datetime.strptime(data['date'][ind], format_ddmmyyyy)) and \
					isinstance(data['№'][ind], numpy.int64) and \
					data['client_name'][ind] and data['client_org'][ind]:
				new_bill: BillCreate = BillCreate(client_name=data['client_name'][ind],
				                                  client_org=data['client_org'][ind],
				                                  number=int(data['№'][ind]),
				                                  sum=float(data['sum'][ind]),
				                                  date=data['date'][ind],
				                                  service=data['service'][ind])
				await bills_repo.create_bill(new_bill=new_bill)

	except Exception as e:
		logger.critical(e)
		return {"message": "There was an error uploading the file"}
	return {"message": f"Successfully uploaded {file.filename}"}


@router.get("/", response_model=List[BillPublic], name="bills:get-all-bills")
async def get_all_bills(
		order_by: str | None = None, client_name: str | None = None, client_org: str | None = None,
		bills_repo: BillsRepository = Depends(get_repository(BillsRepository))) -> list[BillInDB]:
	return await bills_repo.get_all_bills(order_by=order_by, client_name=client_name, client_org=client_org)
