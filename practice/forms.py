from django import forms
# from .models import BlogPostForm

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget = forms.Textarea)

# class BlogPostModelForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'slug', 'content']
