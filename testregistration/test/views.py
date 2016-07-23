# -*- coding: utf-8 -*-
"""Test views."""
from flask import Blueprint, render_template

blueprint = Blueprint('test', __name__, url_prefix='/tests', static_folder='../static')


@blueprint.route('/')
def index():
    """List members."""
    return render_template('tests/index.html')
