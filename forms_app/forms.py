"""
Neon's Form - Dynamic form generation for responses
"""
from django import forms
from .models import Form, Question, Response, Answer, Option


def build_form_from_model(form_model):
    """Build a Django form dynamically from a Form model instance."""
    class DynamicForm(forms.Form):
        pass

    for question in form_model.questions.all():
        field_name = 'question_{}'.format(question.id)
        required = question.required

        if question.question_type == 'text':
            field = forms.CharField(
                max_length=500,
                required=required,
                widget=forms.TextInput(attrs={
                    'class': 'neon-input',
                    'placeholder': 'Your answer',
                })
            )
        elif question.question_type == 'textarea':
            field = forms.CharField(
                required=required,
                widget=forms.Textarea(attrs={
                    'class': 'neon-input neon-textarea',
                    'placeholder': 'Your answer',
                    'rows': 4,
                })
            )
        elif question.question_type in ('radio', 'dropdown'):
            choices = [(opt.id, opt.text) for opt in question.options.all()]
            widget = forms.RadioSelect(attrs={'class': 'neon-radio'}) if question.question_type == 'radio' else forms.Select(attrs={'class': 'neon-select'})
            field = forms.ChoiceField(
                choices=choices,
                required=required,
                widget=widget
            )
        elif question.question_type == 'checkbox':
            choices = [(opt.id, opt.text) for opt in question.options.all()]
            field = forms.MultipleChoiceField(
                choices=choices,
                required=required,
                widget=forms.CheckboxSelectMultiple(attrs={'class': 'neon-checkbox'})
            )
        else:
            field = forms.CharField(required=required, widget=forms.TextInput(attrs={'class': 'neon-input'}))

        field.label = question.text
        DynamicForm.base_fields[field_name] = field

    return DynamicForm
