"""
Neon's Form - Models for form creation and responses
"""
from django.db import models


class Form(models.Model):
    """A form that contains questions."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Question(models.Model):
    """A question within a form."""
    QUESTION_TYPES = (
        ('text', 'Short Text'),
        ('textarea', 'Long Text'),
        ('radio', 'Single Choice'),
        ('checkbox', 'Multiple Choice'),
        ('dropdown', 'Dropdown'),
    )
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='text')
    required = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text[:50]


class Option(models.Model):
    """Options for radio, checkbox, or dropdown questions."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text


class Response(models.Model):
    """A submitted response to a form."""
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='responses')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Response to {} at {}'.format(self.form.title, self.submitted_at)


class Answer(models.Model):
    """An answer to a specific question within a response."""
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.TextField(blank=True)
    selected_options = models.ManyToManyField(Option, blank=True, related_name='answers')

    def __str__(self):
        if self.text_answer:
            return self.text_answer[:50]
        return ', '.join(o.text for o in self.selected_options.all()[:3])
