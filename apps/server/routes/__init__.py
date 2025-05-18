from .sql import router as sql_router
from .table import router as table_router

all_routers = [
    sql_router,
    table_router,
]
