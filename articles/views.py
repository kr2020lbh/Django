from django.shortcuts import render,redirect
from .models import Article,Comment
from .forms import ArticleForm,CommentForm
# Create your views here.

def index(request):
  articles = Article.objects.all()
  length = len(articles)
  last_idx = length-1
  context = {
    'articles' : articles,
    'length' : length,
    'last_idx' : last_idx,
  }
  return render(request,'articles/index.html',context)

def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save()
      return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm()
  context = {
    'form' : form,
  }
  return render(request,'articles/create.html',context)


def detail(request,article_pk):
  article = Article.objects.get(pk=article_pk)
  comment_form = CommentForm()
  comments = article.comment_set.all()

  '''
  comments = []
  for comment in Comment.object.all():
    if comment.article_id == article_pk:
      comments.append(comment)
  '''
  context = {
    'article' : article,
    'comment_form' : comment_form,
    'comments' : comments,
  }
  return render(request,'articles/detail.html',context)


def update(request,article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.method == 'POST':
    form = ArticleForm(data=request.POST,instance=article)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', article.pk)
      
  else:
    form = ArticleForm(instance=article)
  context = {
    'form' : form,
    'article' : article,
  }
  return render(request,'articles/update.html',context)


def delete(request,article_pk):
  if request.method == 'POST':
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')


def comment_create(request,article_pk):
  article = Article.objects.get(pk=article_pk)
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid():
    comment = comment_form.save(commit=False)
    comment.article = article
    comment.save()
    return redirect('articles:detail',article.pk)
  context = {
    'article':article,
    'comment_form':comment_form,
  }
  return render(request,'articles/detail.html',context)


def comment_delete(request,article_pk,comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()
  return redirect('articles:detail',article_pk)