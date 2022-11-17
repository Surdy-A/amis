from django.shortcuts import render
from member.models import Member
from blog.models import Blog


def home(request):
    latest_posts = Blog.objects.all()[:5]
    members = Member.objects.all()
    print("members: ", latest_posts)

    return render(
        request, 'index.html', {
            'posts': latest_posts,
            'members': members,
        })

