import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_website.settings')

import django
django.setup()

import random
from userLogin.models import User
from faker import Faker 

fakegen = Faker()

def populate(N = 5):

	for N in range(N):
		name = fakegen.name()
		email = str(fakegen.email())

		# first_name, last_name = str(fake_name).split(' ')

		# Put the above data in the database
		user = User.objects.get_or_create(name = name,
			email = email)[0]

if __name__ == '__main__':
	print('Populating script!')
	populate(30)
	print('DONE!')