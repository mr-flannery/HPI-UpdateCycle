from update_cycle.models import Page
from django.forms import ModelForm, DateInput
 
class PostPageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['name', 'url', 'comment', 'contact_person', 'next_update_at']