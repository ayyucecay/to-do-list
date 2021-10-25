# Main Imports

# Django Imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports
from .models import check_list


def random_view(request):
    """
    In this view the users can see the landing page of the website which
    holds a basic single page app of a TODO application
    """

    # Getting all of the check boxes to list and display them
    try:
        all_todo_items = check_list.objects.all().order_by("-id")
    except ObjectDoesNotExist:
        all_todo_items = None

    # Getting today and date

    # Creating a new todo checkbox form processing
    empty_input = False

    if request.POST.get("add_task_form_submit"):
        todo_content = request.POST.get("todo_content")

        # check if todo check content is empty or not
        if bool(todo_content) == False or todo_content == "":
            empty_input = True
        else:
            new_todo = check_list(
                todo_content=todo_content,
            )
            new_todo.save()
            return HttpResponseRedirect("/")

    # Checking the todo box form processing




    data = {
        'all_items': all_todo_items,
        "empty_input": empty_input,
    }

    return render(request, 'main.html', data)


# todo_daily


# todo_weekly


# todo_monthly


# todo_yearls
