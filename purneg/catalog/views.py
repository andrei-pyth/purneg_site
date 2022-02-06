from django.shortcuts import render
from .models import Article, Client, Contacts
from django.views import generic

def index(request):
    num_clients = Client.objects.all().count()
    num_articles = Article.objects.all().count()
    num_contacts = Contacts.objects.count()

    context = {
            'num_clients':num_clients,
            'num_articles':num_articles,
            'num_contacts':num_contacts
    }

    return render(request, 'index.html', context=context)

class ArticleListView(generic.ListView):
    model = Article

class ArticleDetailView(generic.DetailView):
    model = Article
