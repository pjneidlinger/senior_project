from flask import render_template, redirect, url_for
from app import app
from app.forms import IndexForm

@app.route('/index', methods=['GET', 'POST'])

def index():
    form = IndexForm()
    if form.validate_on_submit():
	return redirect(url_for('index'), points = form.points.data, rebounds = form.rebounds.data, assists = form.assists.data, steals = form.steals.data, blocks = form.blocks.data, three = form.threes.data, fgp = form.fgp.data, fga = form.fga.data, ftp = form.ftp.data, fta = form.fta.data, turnovers = form.turnovers.data)
    return render_template('index.html', title='Home', form=form)
