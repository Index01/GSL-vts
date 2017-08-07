

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
#        dt = elem['UTC']
        idTag = elem['tagID']
#        playaName = 'Index'

        check_for_existing_id(idTag)


#        person = GatePersonnel(playaName=playaName , additionalIdentifier="ping pong" , 
#                 firstPublishedEntryDate= dt , lastPublishedEntryDate= dt) 
#        rfidTag = RfidTag(tagID= idTag, firstDate= dt, lastDate= dt) 

#        person = GatePersonnel(playaName=playaName) 
        rfidTag = RfidTag(tagID=idTag) 
        
#        db.session.add(person)
        db.session.add(rfidTag)
        db.session.commit()

def check_for_existing_id(tagID):
    #status = db.session.query(exists().where(RfidTag.tagID==tagID)).scalar()
    #print status
    print "checking db..." 
    return 
