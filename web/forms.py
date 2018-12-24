from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, PasswordField, BooleanField, \
SubmitField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, InputRequired, Optional
from wtforms.widgets import TextArea


class AlignmentForm(FlaskForm):
    target_seq = TextAreaField(
        'target_sequence',
        widget=TextArea(),
        validators=[DataRequired()],
        render_kw={
            "rows": 10,
            "cols": 7
        })
    query_seq = TextAreaField(
        'query_sequence',
        widget=TextArea(),
        validators=[DataRequired()],
        render_kw={
            "rows": 10,
            "cols": 7
        })
    submit = SubmitField('Alginments!')


MASS_CHOICES = [(1.0, 'mg'), (0.001, 'ug'), (0.000001, 'ng')]
VOL_CHOICES = [(1.0, 'ml'), (0.001, 'ul'), (0.000001, 'nl')]


class ConversionForm(FlaskForm):
    molecular_weight = FloatField(validators=[InputRequired()])
    mass = FloatField(validators=[InputRequired()])
    mass_unit = SelectField(
        choices=MASS_CHOICES, validators=[Optional()], coerce=float)
    volume = FloatField(validators=[InputRequired()])
    volume_unit = SelectField(
        choices=VOL_CHOICES, validators=[Optional()], coerce=float)
    submit = SubmitField('Submit!')


class BufferForm(FlaskForm):
    molecular_weight = FloatField(validators=[InputRequired()])
    molar = FloatField(validators=[InputRequired()])
    molar_unit = SelectField(
        choices=[(1.0, 'M'), (0.001, 'mM'), (0.000001, 'uM')],
        validators=[Optional()],
        coerce=float)
    volume = FloatField(validators=[InputRequired()])
    volume_unit = SelectField(
        choices=[(1000.0, 'L'), (1.0, 'ml'), (0.001, 'ul')],
        validators=[Optional()],
        coerce=float)
    submit = SubmitField('Submit!')


class BrothForm(FlaskForm):
    volume = StringField('name', validators=[InputRequired()])
    volume_unit = SelectField(
        choices=[(1.0, 'L'), (0.001, 'ml')], coerce=float)
    broth_type = SelectField(
        choices=[(1, 'LB broth'), (2, 'LB Agar'), (3, 'SB broth'),
                 (4, 'SOB broth'), (5, '2xYT broth'), (6, '2xYT-GA broth')],
        coerce=int)
    submit = SubmitField('Calculate!')


class OligoForm(FlaskForm):
    target_seq = TextAreaField(
        'target_sequence',
        widget=TextArea(),
        validators=[DataRequired()],
        render_kw={
            "rows": 4,
            "cols": 10
        })
    submit = SubmitField('Calculate!')


class TranslateForm(FlaskForm):
    target_seq = TextAreaField(
        'target_sequence',
        widget=TextArea(),
        validators=[DataRequired()],
        render_kw={
            "rows": 4,
            "cols": 10
        })
    submit = SubmitField('Translate!')
