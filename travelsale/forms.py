from django import forms

from travelsale.models import Travelproduct, Type, Destination, Order, Payment, Staff, Customer


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_job_position(self):
        return self.cleaned_data['job_position'].strip()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_travel_date(self):
        return self.cleaned_data['travel_date'].strip()


class TravelproductForm(forms.ModelForm):
    class Meta:
        model = Travelproduct
        fields = '__all__'

    def clean_travelproduct_name(self):
        return self.cleaned_data['travelproduct_name'].strip()

    def clean_price(self):
        return self.cleaned_data['price']

    def clean_discount(self):
        return self.cleaned_data['discount']

    def clean_duration(self):
        return self.cleaned_data['duration']

    def clean_description(self):
        return self.cleaned_data['description'].strip()


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

    def clean_type_name(self):
        return self.cleaned_data['type_name'].strip()


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'

    def clean_destination_name(self):
        return self.cleaned_data['destination_name'].strip()


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'