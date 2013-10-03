from django.contrib.auth.models import User, check_password

class MomoBackend(object):
	def authenticate(self, username = None, password = None):
		user = User.objects.get(username = username)
		pwd_valid = check_password(password, user.password)
		if pwd_valid:
			return user
		return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk = user_id)
		except User.DoesNotExist:
			return None

