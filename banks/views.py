from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Bank, Branch
from .forms import BankForm, BranchForm

def list_banks(request):
    banks = Bank.objects.all()
    return render(request, 'banks/list_banks.html', {'banks': banks})

@login_required
def bank_details(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    branches = Branch.objects.filter(bank=bank)
    return render(request, 'banks/bank_details.html', {'bank': bank, 'branches': branches})

@login_required
def add_branch(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.bank = bank
            branch.save()
            return redirect('branch_details', branch_id=branch.id)
    else:
        form = BranchForm()
    return render(request, 'banks/add_branch.html', {'form': form})

def branch_details(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    data = {
        'id': branch.id,
        'name': branch.name,
        'transit_num': branch.transit_num,
        'address': branch.address,
        'email': branch.email,
        'capacity': branch.capacity,
        'last_modified': branch.last_modified.isoformat()
    }
    return JsonResponse(data)

@login_required
def edit_branch(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_details', branch_id=branch.id)
    else:
        form = BranchForm(instance=branch)
    return render(request, 'banks/edit_branch.html', {'form': form})
