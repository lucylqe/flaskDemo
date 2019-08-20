from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length

from apps.main import bp
from extension import mysqldb as db


class HelloForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@bp.route('/form', methods=['GET', 'POST'])
def test_form():
    form = HelloForm()
    return render_template('form.html', form=form)


@bp.route('/nav', methods=['GET', 'POST'])
def test_nav():
    return render_template('nav.html')


@bp.route('/pagination', methods=['GET', 'POST'])
def test_pagination():
    from flask_sqlalchemy import Pagination
    pagination = Pagination(query='', page=1, per_page=5, total=19, items=[1,2,3,4])
    messages = pagination.items
    return render_template('pagination.html', pagination=pagination, messages=messages)


@bp.route('/utils', methods=['GET', 'POST'])
def test_utils():
    return render_template('utils.html')