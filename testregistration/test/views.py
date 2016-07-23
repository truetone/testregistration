# -*- coding: utf-8 -*-
"""Test views."""
from flask import Blueprint, render_template
from testregistration.test.models import Test
from testregistration.time_slot.models import TimeSlot

blueprint = Blueprint('test', __name__, url_prefix='/tests', static_folder='../static')


@blueprint.route('/')
def index():
    """List members."""
    # TODO limit by logged in user
    tests = Test.query.all()

    # TODO this is a horrible hack but I don't have the relationship properly
    # configured yet in SQL Alchemy. This should be fixed right away, but some
    # times you just have to hack it to have something to show. :(
    view_tests = []
    for test in tests:
        time_slots = TimeSlot.query.filter(test_id=test.id)
        ts_data = []

        for ts in time_slots:
            ts_data.append({
                'start_time': ts.start_time,
                'end_time': ts.end_time
            })
        view_data = {
            'id': test.id,
            'name': test.name,
            'time_slots': ts_data
        }
        # lines 19-34 should basically go away once I get the relationship right
        view_tests.append(view_data)
    return render_template(
        'tests/index.html',
        tests=view_tests,
    )
