from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from travelsale.forms import TravelproductForm, TypeForm, DestinationForm, OrderForm, PaymentForm, StaffForm, CustomerForm
from travelsale.utils import PageLinksMixin
from travelsale.models import (
    Travelproduct,
    Type,
    Destination,
    Order,
    Payment,
    Staff,
    Customer,
)


class StaffList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Staff
    permission_required = 'travelsale.view_staff'


class StaffDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Staff
    permission_required = 'travelsale.view_staff'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        staff = self.get_object()
        order_list = staff.orders.all()
        context['order_list'] = order_list
        return context


class StaffCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = StaffForm
    model = Staff
    permission_required = 'travelsale.add_staff'


class StaffUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = StaffForm
    model = Staff
    template_name = 'travelsale/staff_form_update.html'
    permission_required = 'travelsale.change_staff'


class StaffDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Staff
    success_url = reverse_lazy('travelsale_staff_list_urlpattern')
    permission_required = 'travelsale.delete_staff'

    def get(self, request, pk):
        staff = get_object_or_404(Staff, pk=pk)
        orders = staff.orders.all()
        if orders.count() > 0:
            return render(
                request,
                'travelsale/staff_refuse_delete.html',
                {'staff': staff,
                 'orders': orders,
                 }
            )
        else:
            return render(
                request,
                'travelsale/staff_confirm_delete.html',
                {'staff': staff}
            )


class OrderList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Order
    permission_required = 'travelsale.view_order'


class OrderDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Order
    permission_required = 'travelsale.view_order'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        order = self.get_object()
        travelproduct = order.travelproduct
        staff = order.staff
        payment_list = order.payments.all()
        context['travelproduct'] = travelproduct
        context['staff'] = staff
        context['payment_list'] = payment_list
        return context


class OrderCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = OrderForm
    model = Order
    permission_required = 'travelsale.add_order'


class OrderUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = OrderForm
    model = Order
    template_name = 'travelsale/order_form_update.html'
    permission_required = 'travelsale.change_order'


class OrderDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('travelsale_order_list_urlpattern')
    permission_required = 'travelsale.delete_order'

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        payments = order.payments.all()
        if payments.count() > 0:
            return render(
                request,
                'travelsale/order_refuse_delete.html',
                {'order': order,
                 'payments': payments,
                 }
            )
        else:
            return render(
                request,
                'travelsale/order_confirm_delete.html',
                {'order': order}
            )


class TravelproductList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Travelproduct
    permission_required = 'travelsale.view_travelproduct'


class TravelproductDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Travelproduct
    permission_required = 'travelsale.view_travelproduct'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        travelproduct = self.get_object()
        type = travelproduct.type
        destination = travelproduct.destination
        order_list = travelproduct.orders.all()
        context['type'] = type
        context['destination'] = destination
        context['order_list'] = order_list
        return context


class TravelproductCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TravelproductForm
    model = Travelproduct
    permission_required = 'travelsale.add_travelproduct'


class TravelproductUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = TravelproductForm
    model = Travelproduct
    template_name = 'travelsale/travelproduct_form_update.html'
    permission_required = 'travelsale.change_travelproduct'


class TravelproductDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Travelproduct
    success_url = reverse_lazy('travelsale_travelproduct_list_urlpattern')
    permission_required = 'travelsale.delete_travelproduct'

    def get(self, request, pk):
        travelproduct = get_object_or_404(Travelproduct, pk=pk)
        orders = travelproduct.orders.all()
        if orders.count() > 0:
            return render(
                request,
                'travelsale/travelproduct_refuse_delete.html',
                {'travelproduct': travelproduct,
                 'orders': orders,
                 }
            )
        else:
            return render(
                request,
                'travelsale/travelproduct_confirm_delete.html',
                {'travelproduct': travelproduct}
            )


class TypeList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Type
    permission_required = 'travelsale.view_type'


class TypeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Type
    permission_required = 'travelsale.view_type'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        type = self.get_object()
        travelproduct_list = type.travelproducts.all()
        context['travelproduct_list'] = travelproduct_list
        return context


class TypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TypeForm
    model = Type
    permission_required = 'travelsale.add_type'


class TypeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = TypeForm
    model = Type
    template_name = 'travelsale/type_form_update.html'
    permission_required = 'travelsale.change_type'


class TypeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Type
    success_url = reverse_lazy('travelsale_type_list_urlpattern')
    permission_required = 'travelsale.delete_type'

    def get(self, request, pk):
        type = get_object_or_404(Type,pk=pk)
        travelproducts = type.travelproducts.all()
        if travelproducts.count() > 0:
            return render(
                request,
                'travelsale/type_refuse_delete.html',
                {'type': type,
                 'travelproducts': travelproducts,
                 }
            )
        else:
            return render(
                request,
                'travelsale/type_confirm_delete.html',
                {'type': type}
            )


class DestinationList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Destination
    permission_required = 'travelsale.view_destination'


class DestinationDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Destination
    permission_required = 'travelsale.view_destination'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        destination = self.get_object()
        travelproduct_list = destination.travelproducts.all()
        context['travelproduct_list'] = travelproduct_list
        return context


class DestinationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = DestinationForm
    model = Destination
    permission_required = 'travelsale.add_destination'


class DestinationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = DestinationForm
    model = Destination
    template_name = 'travelsale/destination_form_update.html'
    permission_required = 'travelsale.change_destination'


class DestinationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Destination
    success_url = reverse_lazy('travelsale_destination_list_urlpattern')
    permission_required = 'travelsale.delete_destination'

    def get(self, request, pk):
        destination = get_object_or_404(Destination,pk=pk)
        travelproducts = destination.travelproducts.all()
        if travelproducts.count() > 0:
            return render(
                request,
                'travelsale/destination_refuse_delete.html',
                {'destination': destination,
                 'travelproducts': travelproducts,
                 }
            )
        else:
            return render(
                request,
                'travelsale/destination_confirm_delete.html',
                {'destination': destination}
            )


class CustomerList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Customer
    permission_required = 'travelsale.view_customer'


class CustomerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Customer
    permission_required = 'travelsale.view_customer'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        customer = self.get_object()
        payment_list = customer.payments.all()
        context['payment_list'] = payment_list
        return context


class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CustomerForm
    model = Customer
    permission_required = 'travelsale.add_customer'


class CustomerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CustomerForm
    model = Customer
    template_name = 'travelsale/customer_form_update.html'
    permission_required = 'travelsale.change_customer'


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('travelsale_customer_list_urlpattern')
    permission_required = 'travelsale.delete_customer'

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        payments = customer.payments.all()
        if payments.count() > 0:
            return render(
                request,
                'travelsale/customer_refuse_delete.html',
                {'customer': customer,
                 'payments': payments,
                 }
            )
        else:
            return render(
                request,
                'travelsale/customer_confirm_delete.html',
                {'customer': customer}
            )


class PaymentList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Payment
    permission_required = 'travelsale.view_payment'


class PaymentDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Payment
    permission_required = 'travelsale.view_payment'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        payment = self.get_object()
        order = payment.order
        customer = payment.customer
        context['order'] = order
        context['customer'] = customer
        return context


class PaymentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PaymentForm
    model = Payment
    permission_required = 'travelsale.add_payment'


class PaymentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PaymentForm
    model = Payment
    template_name = 'travelsale/payment_form_update.html'
    permission_required = 'travelsale.change_payment'


class PaymentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Payment
    success_url = reverse_lazy('travelsale_payment_list_urlpattern')
    permission_required = 'travelsale.delete_payment'