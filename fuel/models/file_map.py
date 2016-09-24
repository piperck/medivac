from fuel.init_db import Base
from sqlalchemy import Column, Integer, String, DateTime


class FileMap(Base):
    __tablename__ = 'file_map'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(100), nullable=False)
    file_extension_name = Column(String(5), nullable=False)
    create_time = Column(DateTime)
    update_time = Column(DateTime)

    def __init__(self, file_name=None):
        self.file_name = file_name

    def __repr__(self):
        return '<file_map %r>' % self.file_name
