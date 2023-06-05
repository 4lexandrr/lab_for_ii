# from pymystem3 import Mystem


# sentence = ['Я люблю 311 кафедру!',
#             'Мама моет окна.',
#             'Собаки бегают по улице.']


# lemmatizer = Mystem()

# for sent in sentence:
#     sent_lemmas = lemmatizer.lemmatize(sent)
#     print(sent_lemmas)

import pymorphy2
 
morph = pymorphy2.MorphAnalyzer()
a = input('Введите существительное: ')
word = morph.parse(a)[0]
if 'NOUN' in word.tag.POS:
    print('Единственное число:')
    print('Именительный падеж:', word.inflect({'nomn'}).word)
    print('Родительный падеж:', word.inflect({'gent'}).word)
    print('Дательный падеж:', word.inflect({'datv'}).word)
    print('Винительный падеж:', word.inflect({'accs'}).word)
    print('Творительный падеж:', word.inflect({'ablt'}).word)
    print('Предложный падеж:', word.inflect({'loct'}).word)
    print('Множественное число:')
    print('Именительный падеж:', word.inflect({'nomn', 'plur'}).word)
    print('Родительный падеж:', word.inflect({'gent', 'plur'}).word)
    print('Дательный падеж:', word.inflect({'datv', 'plur'}).word)
    print('Винительный падеж:', word.inflect({'accs', 'plur'}).word)
    print('Творительный падеж:', word.inflect({'ablt', 'plur'}).word)
    print('Предложный падеж:', word.inflect({'loct', 'plur'}).word)
else:
    print('Не существительное')
    
    
morph = pymorphy2.MorphAnalyzer()
 
word = input('Введите глагол: ')
word = morph.parse(word)[0]
print(word)
pos = word.tag.POS
 
CASES = {
        ('past','<Прошедшее время>'):[
            {'masc'},{'femn'},{'neut'},{'plur'}
        ],
        ('pres','<Настоящее время>'):[
            {'1per','sing'},
            {'1per','plur'},
            {'2per','sing'},
            {'2per','plur'},
            {'3per','sing'},
            {'3per','plur'}
        ]
    }    
 
if word.tag.POS in {'INFN','VERB'}:
    for key,val in CASES.items():
        print(key[1])
        for cases in val:
            cases.add(key[0])
            w = word.inflect(cases).word
            print(w) 
           
else:
    print('Не глагол',pos)