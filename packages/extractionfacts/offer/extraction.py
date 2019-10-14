import re
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(
    __file__)).rsplit('packages')[0] + 'packages')

from datetime import datetime
from jsonencoder import JsonEncoder
from structuralanalysis import ExtractionContact
from structuralanalysis import ExtractionDate
from structuralanalysis import ExtractionProfileType
from structuralanalysis import ExtractionGender
from structuralanalysis import ExtractionContentType
from structuralanalysis import ExtractionCity


class Contacts:
    Email = []
    Phone = []
    Url = []

class JobTextAnalysisResponseContract:
    ContentTypes = []
    Genders = []
    ProfileTypes = [] 
    Contacts = None
    Country = ''
    City = ''
    StartDate = None
    EndDate = None

class ExtractionOffer:
    text = ""

    def __init__(self, text):
        self.text = text
        self

    def remove_tags(self, text):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub(' ', text)

    def remove_highlighters(self, text):
        text = text.replace('!', ' ')
        text = text.replace('()', ' ')
        text = text.replace(')', ' ')
        return text.replace('  ', ' ')

    def getFacts(self):
        facts = JobTextAnalysisResponseContract()
        self.text = self.remove_tags(self.text)
        self.text = self.remove_highlighters(self.text)
        
        facts.ContentTypes = ExtractionContentType(self.text).get()
        facts.Genders = ExtractionGender(self.text).get()
        facts.ProfileTypes = ExtractionProfileType(self.text).get()
        facts.City = ExtractionCity(self.text).get()

        extractionDate = ExtractionDate(self.text)
        extractionDate.getDate()
        if extractionDate.start_date is not None:
            facts.StartDate = extractionDate.start_date.strftime("%d-%m-%Y")
        if extractionDate.end_date is not None:
            facts.EndDate = extractionDate.end_date.strftime("%d-%m-%Y")
        
        extractionContact = ExtractionContact(self.text)
        facts.Contacts = Contacts()
        facts.Contacts.Email = extractionContact.getEmails()
        facts.Contacts.Phone = extractionContact.getPhones()
        facts.Contacts.Url = extractionContact.getUrls()
        return facts

    def getJson(self):        
        contract = self.getFacts()
        return JsonEncoder().convert_to_json(contract)