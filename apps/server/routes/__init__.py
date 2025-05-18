from .sql import router as sql_router
from .table import router as table_router
from .specialization import router as specialization_router
from .teacher import router as teacher_router
from .group import router as group_router
from .subject import router as subject_router

all_routers = [
    sql_router,
    table_router,
	specialization_router,
	teacher_router,
	group_router,
	subject_router
]
