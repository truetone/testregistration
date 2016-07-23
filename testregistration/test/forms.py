# -*- coding: utf-8 -*-
"""Test forms."""
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class TestEntryForm(Form):
    """Register form."""

    name = StringField('Test Name',
                       validators=[DataRequired(), Length(min=3, max=80)])
