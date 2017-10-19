from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
        	attrs={'rows':5, 'placeholder': 'What is in your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']

# The subject in the fields list inside the Meta class
#  is referring to the subject field in the Topic class

#  Now observe that we are defining an extra field named message. 
#  This refers to the message in the Post we want to save.