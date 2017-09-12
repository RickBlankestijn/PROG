leeftijd = input('Hoe oud ben je?')
paspoort = input('heb je een nederlands paspoort?')

if int(leeftijd) >= 18 and (paspoort == 'ja'):
    print('Je mag stemmen.')

else:
    print('Je mag nog niet stemmen.')
