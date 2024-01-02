import sqlalchemy

from db_init import engine,department,employee

with engine.connect() as conn:
    join = employee.join(department, department.c.id == employee.c.department_id)
    # query = sqlalchemy.select(join).where(department.c.name == 'hr')
    # query = sqlalchemy.select(employee).select_from(join).where(department.c.name == 'hr')
    query = sqlalchemy.select(department).select_from(join).where(employee.c.name == 'Rose')
    print(conn.execute(query).fetchall())

