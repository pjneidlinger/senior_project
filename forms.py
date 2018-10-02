from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class IndexForm(FlaskForm):
    points = StringField('Points', validators=[DataRequired()])
    rebounds = StringField('Rebounds', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    steals = StringField('Steals', validators=[DataRequired()])
    blocks = StringField('Blocks', validators=[DataRequired()])
    threes = StringField('Three Pointers Made', validators=[DataRequired()])
    fgp = StringField('Field Goal Percentage', validators=[DataRequired()])
    fga = StringField('Field Goals Attempted', validators=[DataRequired()])
    ftp = StringField('Free Throw Percentage', validators=[DataRequired()])
    fta = StringField('Free Throws Attempted', validators=[DataRequired()])
    turnovers = StringField('Turnovers', validators=[DataRequired()])
    submit = SubmitField('Calculate')
