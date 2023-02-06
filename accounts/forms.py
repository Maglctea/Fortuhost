from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm


class MyCustomLoginForm(LoginForm):
    def login(self, *args, **kwargs):
        # Add your own processing here.
        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class MyCustomSignupForm(SignupForm):
    def login(self, *args, **kwargs):
        # Add your own processing here.
        # You must return the original result.
        return super(MyCustomSignupForm, self).login(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class MyCustomResetPasswordForm(ResetPasswordForm):
    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super(MyCustomResetPasswordForm, self).save(request)
        # Add your own processing here.
        # Ensure you return the original result
        return email_address

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class MyCustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def save(self):
        # Add your own processing here.
        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(MyCustomResetPasswordKeyForm, self).save()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'