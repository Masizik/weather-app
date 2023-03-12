from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'user_name': auth_forms.UsernameField, }


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('user_name', 'email', 'password1', 'password2')
        field_classes = {
            'user_name': auth_forms.UsernameField, }
