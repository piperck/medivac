import datetime
from fuel.init_db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text


class FileMap(Base):
    __tablename__ = 'file_map'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_path = Column(String(100), nullable=False)
    file_extension_name = Column(String(5), nullable=False)
    file_uri = Column(Text(), nullable=False)
    create_time = Column(DateTime, default=datetime.datetime.now())
    update_time = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, file_path, file_extension_name, file_uri):
        self.file_path = file_path
        self.file_extension_name = file_extension_name
        self.file_uri = file_uri

    def __repr__(self):
        return '<file_map %r>' % self.file_name
