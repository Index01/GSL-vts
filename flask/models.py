
"""
   Models for postgres and sqlalchemy which define the BRC Gate RFID automated checkin database.

   Further models may be created using the pattern below. Creation and transactions will be
   handled by the controller files.  
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship
from sqlalchemy_utcdatetime import UTCDateTime
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class GateDBConnection():
    """Right now this class does nothing, maybe it will do something.""" 
    def __init__():
        pass

    def connect_db():
        pass

class GatePersonnel(Base):
    """
        Gate team member record

        There is lots of discussion about using UUIDs as primary key. Despite 
        the performance hit, security is a high priority for us. There are reports 
        for 10x reduction in performance, before we noticed this difference in performance
        during replication though the table would need to grow over several hundred entries. 
    """

    __tablename__= 'gatepersonnel'
    #id = Column()    # IDs? where we're going, we don't need IDs.
    uuid = Column(UUID(as_uuid=True), primary_key=True) 
    playaName = Column(String(64))
    additionalIdentifier = Column(String(64))
    firstPublishedEntryDate = Column(UTCDateTime, default=None)
    lastPublishedEntryDate = Column(UTCDateTime, default=None)
  
    # Define ref for ralationship, on the one side of one to many. 
    currentRfidTagIDs = Column(UUID, ForeignKey('rfidtag.uuid')) 
 
    def __init__(self, name):
        self.name = name 


    def __repr__(self):
        return "<GatePersonnel(PlayaName= '%s')>" % self.name


class RfidTag(Base):
    """
        Gate RFID UTF tag IDs
 
        Same explaination as above regarding UUIDs, security, performance.
    """ 
   
    __tablename__ = 'rfidtag'  
    #id = Column()
    uuid = Column(UUID(as_uuid=True), primary_key=True)  
    rfidTagId = Column(Integer)
    firstPublishedEntryDate = Column(UTCDateTime, default=None)
    lastPublishedEntryDate = Column(UTCDateTime, default=None)

    # Foreign key relationship, one to many, relationship on many side.
    tagHolder = relationship("GatePersonnel", backref="RFIDTag", lazy='select')
 
    def __init__(self, name):
        self.name = name

    
    def __repr__(self):
        return "<RFIDTag(RFIDTagID= '%s')>" % self.name



