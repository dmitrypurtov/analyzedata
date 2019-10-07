import os
import json
import re
from cities import ExtractionCity
from contenttype import ExtractionContentType
from gender import ExtractionGender
from profiletype import ExtractionProfileType
from date import ExtractionDate

class JobTextAnalysisResponseContract:
    ContentTypes = []
    Genders = []
    ProfileTypes = [] 
    Country = ''
    City = ''
    StartDate = None
    EndDate = None

    def __init__(self):
        self

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class ExtractionOffer:
    text = ""

    def __init__(self, text):
        self.text = text
        self

    def remove_tags(self, text):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub(' ', text)

    def remove_highlighters(self, text):
        TAG_RE = text.replace('!', ' ')
        TAG_RE = text.replace('()', ' ')
        TAG_RE = text.replace(')', ' ')
        return TAG_RE.sub(' ', text)

    def getJson(self):
        contract = JobTextAnalysisResponseContract()
        self.text = self.remove_tags(self.text)
        self.text = self.remove_highlighters(self.text)
        
        contract.ContentTypes = ExtractionContentType(self.text).get()
        contract.Genders = ExtractionGender(self.text).get()
        contract.ProfileTypes = ExtractionProfileType(self.text).get()
        contract.cities = ExtractionCity(self.text).get()

        extractionDate = ExtractionDate(self.text)
        extractionDate.getDate()
        contract.StartDate = extractionDate.start_date
        contract.EndDate = extractionDate.end_date

        json = contract.toJSON()
        return json
