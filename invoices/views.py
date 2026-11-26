from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Invoice
from .forms import InvoiceForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
def create_invoice(request):
    Invoice.objects.create(
        customer_name = 'rahul',
        invoice_number = 'INV001',
        amount = 100.00,
        is_paid = True
    )
    return render(request, '/Users/shiramdasuabhiram/Desktop/untitled folder 2/invoices/templates/invoices/invoice_list.html', {})
def show_old_invoices(request):
    invoices = Invoice.objects.get(invoice_number='INV001')
    data = {
        'nvoices': invoices
    }
    return render(request, '/Users/shiramdasuabhiram/Desktop/untitled folder 2/invoices/templates/invoice_detail.html', data)
def mark_invoice_as_paid(request):
    invoice.objects.filter(invoice_number='INV001').update(is_paid=True)
    all_invoices = Invoice.objects.filter(is_paid=False)
def show_unpaid_invoices(request):
    unpaid_invoices = Invoice.objects.filter(is_paid=False)
    data = {
        'unpaid_invoices': unpaid_invoices
    }
    return render(request, '/Users/shiramdasuabhiram/Desktop/untitled folder 2/invoices/templates/invoice_list.html', {})
def show_invoices(request):
    data = {

        'all_invoices': [
            {'customer_name': 'John Doe', 'invoice_number': 'INV001', 'amount': 100.00, 'is_paid': True},
            {'customer_name': 'Jane Smith', 'invoice_number': 'INV002', 'amount': 200.00, 'is_paid': False},
            {'customer_name': 'Alice Johnson', 'invoice_number': 'INV003', 'amount': 150.00, 'is_paid': True},
        ]
    }
    return render(request, 'invoices/invoice_list.html', data)




def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-invoices')
    else:
        form = InvoiceForm()
    
    data = {
        'form':form
    }
    return render(request, 'invoices/add_invoice.html', data)


class HomePageView(TemplateView):
    template_name = 'invoices/home.html'


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoices/invoice_list.html'
    context_object_name = 'all_invoices'


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoices/invoice_detail.html'
    context_object_name = 'invoice'


class InvoiceCreateView(CreateView):
    model = Invoice
    fields = ['customer_name', 'invoice_number', 'amount', 'is_paid']
    template_name = 'invoices/invoice_form.html'
    success_url = '/invoices/'


class InvoiceUpdateView(UpdateView):
    model = Invoice
    fields = ['customer_name', 'invoice_number', 'amount', 'is_paid']
    template_name = 'invoices/invoice_form.html'
    success_url = '/invoices/'


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoices/invoice_confirm_delete.html'
    success_url = '/invoices/'


