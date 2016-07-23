# -*- coding: utf-8 -*-
from testregistration.database import (
    Column, Model, SurrogatePK, db, relationship)


class TimeSlot(SurrogatePK, Model):
    """A time slot for a test."""

    # __tablename__ = 'time_slots'

    start_time = Column(db.DateTime, nullable=False)
    end_time = Column(db.DateTime, nullable=False)
    test_id = Column(db.Integer, db.ForeignKey('test.id'))
    test = relationship('Test',
                        backref=db.backref('time_slot', lazy='dynamic'))

    # def __init__(self, name, **kwargs):
    #     """Create instance."""
    #     db.Model.__init__(self, name=name, **kwargs)

    # def __repr__(self):
    #     """Represent instance as a unique string."""
    #     return '<TimeSlot({name})>'.format(name=self.name)
