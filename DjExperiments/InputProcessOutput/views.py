from django.shortcuts import render
from .forms import blogForm

# Create your views here.

def blog(request):
    title, message = '', ''
    entered = False
    if request.method == 'POST':
        # Form was submitted
        form = blogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name, topic, body = cd['name'], cd['topic'], cd['blogPost']
            title = '{} blogged about "{}"'.format(name, topic)
            message = 'content: {}'.format(body)
            entered = True
    else:
        form = blogForm()

    return render(request,
                  'InputProcessOutput/InputProcessOutput/InputProcessOutput.html',
                  {'form': form,
                   'title': title,
                   'msg': message,
                   'entered': entered}
                  )
