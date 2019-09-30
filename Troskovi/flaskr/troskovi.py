from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('troskovi', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    pretraga = ''
    if request.method == 'POST':
        pretraga = ' WHERE T1.datum_troska BETWEEN "' + request.form['datum_od'] + '" AND "' + request.form['datum_do'] + '"'
    troskovi = db.execute(
        'SELECT T1.id, T1.naziv, T1.datum_troska, T2.naziv As naziv_tipa, T1.iznos '
        ' FROM trosak T1 JOIN tip T2 ON T1.tip = T2.id ' + pretraga
    ).fetchall()
    return render_template('troskovi/index.html', troskovi=troskovi)

@bp.route('/novi', methods=('GET', 'POST'))
def novi():
    if request.method == 'POST':
        tip = request.form['tip']
        naziv = request.form['naziv']
        datum_troska = request.form['datum_troska']
        iznos = request.form['iznos']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO trosak (tip, naziv, datum_troska, iznos)'
                ' VALUES (?, ?, ?, ?)',
                (tip, naziv, datum_troska, iznos)
            )
            db.commit()
            return redirect(url_for('troskovi.index'))
    db = get_db()
    tipovi = db.execute(
        'SELECT *'
        ' FROM tip'
    ).fetchall()
    return render_template('troskovi/novi.html', tipovi=tipovi)