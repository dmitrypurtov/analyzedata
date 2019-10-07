from dataloader import DataLoader
from offer import ExtractionOffer

lines = DataLoader().getTextList()

for line in lines[:21]:
    extractionOffer = ExtractionOffer(line)
    print('----------------------------------------------------------------------')
    print(extractionOffer.getJson())
    print('')
    print(line)
    print('')
    print('')