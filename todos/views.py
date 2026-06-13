from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Todo, Category
from .forms import TodoForm, CategoryForm
from django.contrib.auth.decorators import login_required


@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)

    category_id = request.GET.get('category')
    priority = request.GET.get('priority')
    status = request.GET.get('status')

    if category_id:
        todos = todos.filter(category_id=category_id)
    if priority:
        todos = todos.filter(priority=priority)
    if status == 'completed':
        todos = todos.filter(is_completed=True)
    elif status == 'active':
        todos = todos.filter(is_completed=False)

    context = {
        'todos': todos,
        'categories': categories,
        'total': todos.count(),
        'completed': todos.filter(is_completed=True).count(),
        'active': todos.filter(is_completed=False).count(),
    }
    return render(request, 'todos/index.html', context)


@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Vazifa qo'shildi!")
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/form.html', {'form': form, 'title': "Yangi vazifa"})


@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Vazifa yangilandi!")
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/form.html', {'form': form, 'title': "Vazifani tahrirlash", 'todos': todo})


@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, "Vazifa o'chirildi!")
        return redirect('todo_list')
    return render(request, 'todos/confirm_delete.html', {'todos': todo})


@login_required
def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('todo_list')


@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'todos/categories.html', {'categories': categories})


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kategoriya qo'shildi!")
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'todos/category_form.html', {'form': form, 'title': "Yangi kategoriya"})


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, "Kategoriya o'chirildi!")
        return redirect('category_list')
    return render(request, 'todos/confirm_delete.html', {'category': category})


@login_required
def profile(request):
    context = {
        'total': Todo.objects.filter(user=request.user).count(),
        'completed': Todo.objects.filter(user=request.user, is_completed=True).count(),
        'active': Todo.objects.filter(user=request.user, is_completed=False).count(),
    }
    return render(request, 'account/profile.html', context)
