import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(
    __file__)).rsplit('packages')[0] + 'packages')
    
from dataloader import DataLoader
from extraction import ExtractionOffer

lines = DataLoader().exemple_offers()

for line in lines[:10]:
    extractionOffer = ExtractionOffer(line)
    print('----------------------------------------------------------------------')
    #json = extractionOffer.getJson()
    contract = extractionOffer.getFacts()
    print("Город:",contract.City)
    print("Тип контента:",contract.ContentTypes)
    print("Страна:",contract.Country)
    print("Пол:",contract.Genders)
    print("Тип профиля:",contract.ProfileTypes)
    print("Дата начала:",contract.StartDate)
    print("Дата завершения:", contract.EndDate)
    print("Email:", contract.Contacts.Email)
    print("Phone:", contract.Contacts.Phone)
    print("Url:", contract.Contacts.Url)
    #print("Json:", json)
    print('')
    print(line)
    print('')
    print('')
