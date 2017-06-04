from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from qa.models import Question
from django.core.urlresolvers import reverse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def q_main(request):
    qs = Question.objects.new()
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('q_main') + '?page='

    return render(request, 'list_new.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def popular(request):
    qs = Question.objects.popular()
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'list_rating.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def q_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    return render(request, 'q_detail.html', {
        'question': question,
        'answers': answers,
    })