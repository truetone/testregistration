# -*- coding: utf-8 -*-
"""Test views."""
from flask import Blueprint, render_template
from testregistration.test.models import Test

blueprint = Blueprint('test', __name__, url_prefix='/tests', static_folder='../static')


@blueprint.route('/')
def index():
    """List members."""
    # TODO limit by logged in user
    tests = Test.query.all()
    return render_template(
        'tests/index.html',
        tests=tests,
    )
