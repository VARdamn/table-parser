from sqlalchemy.orm import Session
from app.db.models import Specialization, Group, Subject, Teacher


def seed_initial_data(db: Session):
    specializations = [
        {"name": "Прикладная информатика", "code": "НПИ"},
        {"name": "Прикладная математика и информатика", "code": "НПМ"},
        {"name": "Математика и компьютерные науки", "code": "НКН"},
        {"name": "Бизнес-информатика", "code": "НБИ"},
        {"name": "Фундаментальная информатика и информационные технологии", "code": "НФИ"},
    ]
    for spec in specializations:
        if not db.query(Specialization).filter_by(code=spec["code"]).first():
            db.add(Specialization(**spec))
    db.commit()

    groups = [
        {"group_name": "НПИбд-01-24", "group_code": "НПИбд-01-24"},
        {"group_name": "НПИбд-01-22", "group_code": "НПИбд-01-22"},
        {"group_name": "НПМбд-01-23", "group_code": "НПМбд-01-23"},
        {"group_name": "НКНбд-01-22", "group_code": "НКНбд-01-22"},
        {"group_name": "НПИбд-02-23", "group_code": "НПИбд-02-23"},
    ]
    for group in groups:
        if not db.query(Group).filter_by(group_code=group["group_code"]).first():
            db.add(Group(**group))
    db.commit()

    subjects = [
        {"name": "Математический анализ", "code": "МАТАН"},
        {"name": "Линейная алгебра", "code": "ЛИНАЛ"},
        {"name": "Реляционные базы данных", "code": "РБД"},
        {"name": "Сетевые технологии", "code": "СЕТИ"},
        {"name": "Управление ИТ-сервисами и контентом", "code": "УИТС"},
        {"name": "Теория вероятностей и математическая статистика", "code": "ТВИМС"},
        {"name": "Методы машинного обучения", "code": "ММО"},
        {"name": "Операционные системы", "code": "ОС"},
    ]
    for subject in subjects:
        if not db.query(Subject).filter_by(code=subject["code"]).first():
            db.add(Subject(**subject))
    db.commit()

    teachers = [
        {"full_name": "Иванов Петр Сергеевич", "short_name": "Иванов П.С.", "employee_number": "T001"},
        {"full_name": "Петрова Мария Ивановна", "short_name": "Петрова М.И.", "employee_number": "T002"},
        {"full_name": "Сидоров Алексей Владимирович", "short_name": "Сидоров А.В.", "employee_number": "T003"},
        {"full_name": "Кузнецова Елена Дмитриевна", "short_name": "Кузнецова Е.Д.", "employee_number": "T004"},
        {"full_name": "Смирнов Дмитрий Анатольевич", "short_name": "Смирнов Д.А.", "employee_number": "T005"},
    ]
    for teacher in teachers:
        if not db.query(Teacher).filter_by(employee_number=teacher["employee_number"]).first():
            db.add(Teacher(**teacher))
    db.commit()
