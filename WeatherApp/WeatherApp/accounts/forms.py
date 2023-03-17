from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Fieldset, Submit
from django.contrib.auth import forms as auth_forms, get_user_model
from django.urls import reverse_lazy

UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'username': auth_forms.UsernameField, }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'editUser'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse_lazy('user edit')
        self.helper.field_class = 'form-control form-control-lg'
        self.helper.label_class = 'form-label'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Div(
                            Div(
                                HTML(
                                    """<i class="fas fa-crow fa-2x me-3 pt-5 mt-xl-4" style="color: #709085;"></i>
          <span class="h1 fw-bold mb-0">Logo</span>"""),
                                Div(
                                    Fieldset(

                                        'Edit', 'id', 'first_name', 'last_name', 'email', 'picture'

                                    ),
                                    Div(
                                        Submit('submit', 'Edit', css_class='btn btn-info btn-lg btn-block'),

                                        css_class='pt-1 mb-4',
                                    ),
                                ),
                                css_class='d-flex align-items-center h-custom-2 px-5 ms-xl-4 mt-5 pt-5 pt-xl-0 mt-xl-n5'
                            ), css_class='px-5 ms-xl-4'
                        ), css_class='col-sm-6 text-black'
                    ), css_class='row'
                ), css_class='container-fluid'

            ),

        ),


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'username': auth_forms.UsernameField, }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'CreateUser'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse_lazy('register user')
        self.helper.field_class = 'form-control form-control-lg'
        self.helper.label_class = 'form-label'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Div(
                            Div(
                                HTML(
                                    """<i class="fas fa-crow fa-2x me-3 pt-5 mt-xl-4" style="color: #709085;"></i>
          <span class="h1 fw-bold mb-0">Logo</span>"""),
                                Div(
                                    Fieldset(

                                        'Registration', 'username', 'email', 'password1', 'password2',

                                    ),
                                    Div(
                                        Submit('submit', 'Register', css_class='btn btn-info btn-lg btn-block'),
                                        HTML("""<p class="small mb-5 pb-lg-2"><a class="text-muted" href="#!">Forgot password?</a></p>
            <p>Don't have an account? <a href="#!" class="link-info">Register here</a></p>"""),

                                        css_class='pt-1 mb-4',
                                    ),
                                ),
                                css_class='d-flex align-items-center h-custom-2 px-5 ms-xl-4 mt-5 pt-5 pt-xl-0 mt-xl-n5'
                            ), css_class='px-5 ms-xl-4'
                        ), css_class='col-sm-6 text-black'
                    ), css_class='row'
                ), css_class='container-fluid'

            ),

        ),
