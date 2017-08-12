

import json
from sqlalchemy.sql import exists
from helpfulDecorators import json_attribs_check
from models import GatePersonnel, RfidTag
from config import db
 
@json_attribs_check
def buffer_values(jsonStr):
    jdGslvts = json.loads(jsonStr)
    print jdGslvts 
    for elem in jdGslvts:
        print elem
        dt = elem['UTC']
        idTag = elem['tagID']
#        playaName = 'Index'

        if check_for_existing_id(elem):
            print "adding tag"
             
            rfidTag = RfidTag(tagID=idTag, firstDate=dt) 
            db.session.add(rfidTag)
            db.session.commit()
       
        else:
            print "not adding tag"


#        person = GatePersonnel(playaName=playaName , additionalIdentifier="ping pong" , 
#                 firstPublishedEntryDate= dt , lastPublishedEntryDate= dt) 
#        rfidTag = RfidTag(tagID= idTag, firstDate= dt, lastDate= dt) 

#        person = GatePersonnel(playaName=playaName) 
        
#        db.session.add(person)

def check_for_existing_id(dGslvt):
    if db.session.query(exists().where(RfidTag.rfidTagId==dGslvt['tagID'])).scalar():
        return None   
    else:
         
        if db.session.query(exists().where(RfidTag.firstPublishedEntryDate==None)).scalar():
            setup_new_tag(dGslvt)
        else:
            return dGslvt
    return

def setup_new_tag(**newGslvt):
    pass
 
