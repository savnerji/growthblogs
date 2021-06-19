from django import forms
from .models import Post,Category
from django.forms import Textarea
from django.forms.widgets import Widget

Cat=Category.objects.all().values('category')
Catlist=[]
for obj in Cat:
    Catlist.append((obj['category'],obj['category']))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('heading','category','body')
        widgets={
            'heading':Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(choices=Catlist,attrs={'class':'form-control'}),
        }

