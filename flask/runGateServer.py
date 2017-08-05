#~*~ coding: utf-8 ~*~
#!/usr/bin/env/ python


from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

from config import app
from forms import TagForm
from models import GatePersonnel, RfidTag
 

db = SQLAlchemy(app)

@app.route('/')
def starfighter():
    return 'WELCOME STARFIGHTER'


@app.route('/success')
def success():
    return '[+] Record updated'


@app.route('/Z2F0ZUF1dG9tYXRlZENoZWNraW4=')
def gate_rfid_server():
    return '[+] Automated checkin endpoint'


@app.route('/forms', methods=('GET', 'POST'))
def submit_tag_form():
    form = TagForm()

    #TODO: This conditional seems to always == else
    if form.validate_on_submit():
        return redirect('/success')
    else:
        print 'record updating...'
        print 'Form Data: %s' % request.form.get('name')
        print 'Form Data: %s' % request.form
        return render_template('submit.html', form=form)










if __name__=='__main__':
    #starfighter()
    app.run(debug=True, host='0.0.0.0')
