#!/usr/bin/env python3
"""app/models module"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from models.user import User, Base
from config import user, password, host, port, database


class DB:
    """Database Class"""
    
    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine(f'mysql://{user}:{password}@{host}:{port}/{database}')
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None
    
    @property
    def _session(self):
        """memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
    
    def add_user(self, email: str, hashed_password: str) -> User:
        """Add new user to database
        Args:
            email (str): user email
            hashed_password (str): user hashed_password
        Returns:
            User: User object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user
    
    def find_user_by(self, **kwargs) -> User:
        """Find user by arbitrary keyword arguments.
        Args:
            **keyword: Arbitrary keyword arguments for filtering.
        Returns:
            User: The first User object found.
        Raises:
            NoResultFound: If no user matches the criteria.
            InvalidRequestError: If invalid query arguments are provided.
        """
        if not kwargs:
            raise InvalidRequestError("No quert arument provided")
        query = self._session.query(User)

        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise InvalidRequestError(f"Invalid!. Cannot search user by {key}")
            query = query.filter(getattr(User, key) == value)
        
        user = query.first()
        if user is None:
            raise NoResultFound("No User found matching this criteria")
        return user
            