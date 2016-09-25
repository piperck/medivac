import datetime
from fuel.init_db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text


class FileMap(Base):
    __tablename__ = 'file_maps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(100), nullable=False)
    file_extension_name = Column(String(5), nullable=False)
    file_uri = Column(Text(), nullable=False)
    short_url = Column(String(10), nullable=False, index=True)
    create_time = Column(DateTime, default=datetime.datetime.now())
    update_time = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, file_name, file_extension_name, file_uri, short_url):
        self.file_name = file_name
        self.file_extension_name = file_extension_name
        self.file_uri = file_uri
        self.short_url = short_url

    def __repr__(self):
        return '<file_maps %r>' % self.file_name
