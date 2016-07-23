# -*- coding: utf-8 -*-
from testregistration.database import (
    Column, Model, SurrogatePK, db, relationship)


class Test(SurrogatePK, Model):
    """A test, as in test taken in a classroom."""

    # __tablename__ = 'tests'
    name = Column(db.String(80), nullable=False)

    # TODO obtain and save user info from authentication

    # TODO figure out how to properly define this relationship
    # time_slots = relationship('TimeSlot',
    #                           backref=db.backref('test', lazy='dynamic'))

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Test({name})>'.format(name=self.name)
