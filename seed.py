from models import db, Pet
from app import app

# drop and create tables
db.drop_all()
db.create_all()

# empty tables
Pet.query.delete()

#add pets

whiskey=Pet(name ='Whiskey', species='dog', photo_url='https://images.unsplash.com/photo-1561037404-61cd46aa615b?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8ZG9nfGVufDB8fDB8&auto=format&fit=crop&w=800&q=60', age = '16', notes='looking for love')
rockey=Pet(name ='Rockey', species='dog', photo_url='https://images.unsplash.com/photo-1598133893773-de3574464ef0?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8YnVsbGRvZ3xlbnwwfHwwfA%3D%3D&auto=format&fit=crop&w=800&q=60', age = '2', notes='The Italian Stalian, bulldog')
bravo=Pet(name ='Bravo', species='gecko', photo_url='', age = '6', notes='https://images.unsplash.com/photo-1567530567652-73acb695f408?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8Nnx8Z2Vja298ZW58MHx8MHw%3D&auto=format&fit=crop&w=800&q=60')
crocubot=Pet(name ='crocubot', species='crocodile + cyborg', photo_url='https://static.wikia.nocookie.net/rickandmorty/images/6/68/Crocubot.png/revision/latest/top-crop/width/360/height/450?cb=20170814044646', age = '8', notes='more crock than bot')
wiskers=Pet(name ='Wiskers', species='cat', photo_url='', age = '2', notes='')

db.session.add(whiskey)
db.session.add(rockey)
db.session.add(bravo)
db.session.add(crocubot)
db.session.add(wiskers)

db.session.commit()