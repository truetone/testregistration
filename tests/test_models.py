# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime as dt

import pytest

from testregistration.user.models import Role, User
from testregistration.test.models import Test
from testregistration.time_slot.models import TimeSlot

from .factories import UserFactory


@pytest.mark.usefixtures('db')
class TestUser:
    """User tests."""

    def test_get_by_id(self):
        """Get user by ID."""
        user = User('foo', 'foo@bar.com')
        user.save()

        retrieved = User.get_by_id(user.id)
        assert retrieved == user

    def test_created_at_defaults_to_datetime(self):
        """Test creation date."""
        user = User(username='foo', email='foo@bar.com')
        user.save()
        assert bool(user.created_at)
        assert isinstance(user.created_at, dt.datetime)

    def test_password_is_nullable(self):
        """Test null password."""
        user = User(username='foo', email='foo@bar.com')
        user.save()
        assert user.password is None

    def test_factory(self, db):
        """Test user factory."""
        user = UserFactory(password='myprecious')
        db.session.commit()
        assert bool(user.username)
        assert bool(user.email)
        assert bool(user.created_at)
        assert user.is_admin is False
        assert user.active is True
        assert user.check_password('myprecious')

    def test_check_password(self):
        """Check password."""
        user = User.create(username='foo', email='foo@bar.com',
                           password='foobarbaz123')
        assert user.check_password('foobarbaz123') is True
        assert user.check_password('barfoobaz') is False

    def test_full_name(self):
        """User full name."""
        user = UserFactory(first_name='Foo', last_name='Bar')
        assert user.full_name == 'Foo Bar'

    def test_roles(self):
        """Add a role to a user."""
        role = Role(name='admin')
        role.save()
        user = UserFactory()
        user.roles.append(role)
        user.save()
        assert role in user.roles


@pytest.mark.usefixtures('db')
class TestTest:
    def test_create(self):
        test = Test.create(
            name='Test Test'
        )
        assert test is not None
        assert test.name == 'Test Test'

        retrieved = Test.get_by_id(test.id)
        assert retrieved == test


@pytest.mark.usefixtures('db')
class TestTimeSlot:
    def test_create(self):
        test = Test.create(
            name='Test Test'
        )
        time_slot = TimeSlot.create(
            start_time=dt.datetime.now(),
            end_time=dt.datetime.now() + dt.timedelta(hours=1),
            test_id=test.id,
        )
        assert time_slot is not None
        retrieved = TimeSlot.get_by_id(time_slot.id)
        assert retrieved == time_slot
        assert retrieved.test_id == test.id
