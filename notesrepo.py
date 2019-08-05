'''
	REPOSITORY MONGODB
'''
from pymongo import MongoClient


CLIENT = MongoClient('mongodb://%s:%s@127.0.0.1' % ("admin", "admin"))
COLLECTION = CLIENT.notes


def notes_create(note):
	'''
		INSERT NOTE IN REPOSITORY
	'''
	print(type(note))
	posts = COLLECTION.posts
	post_id = posts.insert_one(note).inserted_id
	return post_id
