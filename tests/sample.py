import os


class UserService:
    pass


class AuthService:

    def authenticate(self):
        service = UserService()
        return service


class PaymentService:

    def process_payment(self):
        auth = AuthService()
        return auth