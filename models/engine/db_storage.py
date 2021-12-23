#!usr/bin/python3
''' STORAGE for when the Engine is based on SQL '''

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review

class DBStorage:
    """ This class manages MySQL storages using SQLAlchemy
    Attributes:
        __engine: engine object
        __session: session object
    """
    __engine = None
    __session = None
    hbnb_classes = {
        'City': City, 'User': User,
        'Place': Place, 'State': State,
    }
    def __init__(self):
        ''' DataBase Storage Constructor '''
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session
        all objects depending of the class name
        """
        newdict = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                newdict[cls + "." + obj.id] = obj
        else:
            for key, value in self.hbnb_classes.items():
                try:
                    query = self.__session.query(value).all()
                except:
                    pass
                for obj in query:
                    newdict[key + "." + obj.id] = obj

        return newdict

    def new(self, obj):
        ''' Add's the object to the current database session '''
        self.__session.add(obj)

    def delete(self, obj=None):
        ''' Delete from the current database session obj if not None '''
        if obj is not None:
            self.__session.delete(obj)

    def save(self):
        '''  Commit's all changes of the current database session '''
        self.__session.commit()

    def reload(self):
        ''' Create's all tables in the database (feature of SQLAlchemy) '''
        Base.metadata.create_all(self.__engine)
        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session()
