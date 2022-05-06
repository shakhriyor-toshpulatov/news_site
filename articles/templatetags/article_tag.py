from django import template

from articles.models import Category, Post

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('templatetags/last_news.html')
def get_last_news(count=4):
    news = Post.objects.order_by('id')[:count].select_related('category')
    news1 = Post.objects.order_by('id')[count:].select_related('category')
    return {'last_news': news, 'news': news1}
