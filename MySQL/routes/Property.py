from typing import Optional, List
from fastapi import APIRouter
from app import utils, schemas

router = APIRouter()

@router.post("/property", response_model=List[schemas.Property])
def get_property(filters: schemas.PropertyRequest):
    query = "SELECT p.address,p.city,s.name,p.price,p.description FROM habi_db.property p inner join status_history sh on p.id = sh.property_id inner join status s on sh.status_id = s.id "
    filtersProp = f"where p.`year` like concat('%','{filters.year}','%') and p.city like concat('%','{filters.city}','%') and s.name like concat('%','{filters.state}','%') and s.name in ('pre_venta', 'en_venta','vendido')"
    query = f"{query} {filtersProp}"
    dbcon = utils.Db()
    r = dbcon.execute(query)
    return r
