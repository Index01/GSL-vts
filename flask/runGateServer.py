#~*~ coding: utf-8 ~*~
#!/usr/bin/env/ python


from flask import Flask, request, render_template, json, Response
from config import app, db
from forms import TagForm, HiddenForm
from models import GatePersonnel, RfidTag
from controllers import buffer_values 

#db = SQLAlchemy(app)



@app.route('/')
def starfighter():
    return 'WELCOME STARFIGHTER'


@app.route('/success')
def success():
    return '[+] Record updated'


@app.route('/Z2F0ZUF1dG9tYXRlZENoZWNraW4=', methods=('GET','POST'))
def gate_rfid_server():
    
    request.accept_mimetypes['application/json']
    if request.is_json: 
        print 'Request Data: %s' % request.data
        print 'JSON Data: %s' % request.json
        try:        
            #buffer_values(request.get_json)
            buffer_values(request.data)

            return Response(status=200) 
        except AttributeError:
            return Response(status=451)
 
    else:
        return Response(status=415)


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
    #app.run(debug=True, host='0.0.0.0')
    print "[+] Creating DBs" 
    db.create_all() 
    app.run(debug=True)
