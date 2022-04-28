from django.http import HttpResponse
from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from roll_paper.models import RollPaper
from accounts.models import User

from .forms import RollPaperForm

# Create your views here.

def userlst(request):
    user_lst = User.objects.only('nickname')
    context = {
        'user_lst': user_lst
    }
    return render(request, 'roll_paper/user_lst.html', context)

# @require_http_methods(['GET', 'POST'])
# @login_required
def write(request):

    if request.method == 'POST':
        form = RollPaperForm(request.POST)
        if form.is_valid():
            rollpaper = form.save(commit=False)
            rollpaper.author = request.user
            rollpaper.save()

            messages.add_message(request, messages.INFO, '편지가 성공적으로 작성되었습니다.')
            return redirect('rollpaper:user_lst')

    else:
        form = RollPaperForm()

    context = {
        'form': form,
    }
    return render(request, 'roll_paper/write.html', context)

def detail(request, rollpaper_pk):
    rollpaper = get_object_or_404(RollPaper, pk=rollpaper_pk)
    context = {
        'rollpaper': rollpaper,
    }
    return render(request, 'roll_paper/detail.html', context)


def udpate(request, rollpaper_pk):
    rollpaper = get_object_or_404(RollPaper, pk=rollpaper_pk)

    if request.method == 'POST':
        form = RollPaperForm(request.POST, instance=rollpaper)
        if form.is_valid():
            form.save()
            return redirect('roll_paper:detail', rollpaper.pk)
    else:
        form = RollPaperForm(instance=rollpaper)

    context = {
        'form': form,
    }

    return render(request, 'roll_paper/update.html', context)

@login_required
@require_http_methods(['POST'])
def delete(request, rollpaper_pk):
    if not request.user.is_authenticated:
        return HttpResponse('권한이 없습니다', status=401)
    
    rollpaper = get_object_or_404(RollPaper, pk=rollpaper_pk)
    rollpaper.delete()
    messages.add_message(request, messages.ERROR, '편지가 성공적으로 삭제되었습니다!')
    return redirect('roll_paper:user_lst')
    
