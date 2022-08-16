from django.urls import path
from travelsale.views import (
    StaffList,
    OrderList,
    TravelproductList,
    TypeList,
    DestinationList,
    CustomerList,
    PaymentList,
    StaffDetail,
    OrderDetail,
    TypeDetail,
    DestinationDetail,
    TravelproductDetail,
    CustomerDetail,
    PaymentDetail,
    StaffCreate,
    OrderCreate,
    TravelproductCreate,
    TypeCreate,
    DestinationCreate,
    CustomerCreate,
    PaymentCreate,
    StaffUpdate,
    OrderUpdate,
    TravelproductUpdate,
    TypeUpdate,
    DestinationUpdate,
    PaymentUpdate,
    CustomerUpdate,
    PaymentDelete,
    StaffDelete,
    OrderDelete,
    TravelproductDelete,
    TypeDelete,
    DestinationDelete,
    CustomerDelete,
)


urlpatterns = [
    path('staff/',
         StaffList.as_view(),
         name='travelsale_staff_list_urlpattern'),

    path('staff/<int:pk>/',
         StaffDetail.as_view(),
         name='travelsale_staff_detail_urlpattern'),

    path('staff/create/',
         StaffCreate.as_view(),
         name='travelsale_staff_create_urlpattern'),

    path('staff/<int:pk>/update/',
         StaffUpdate.as_view(),
         name='travelsale_staff_update_urlpattern'),

    path('staff/<int:pk>/delete/',
         StaffDelete.as_view(),
         name='travelsale_staff_delete_urlpattern'),

    path('order/',
         OrderList.as_view(),
         name='travelsale_order_list_urlpattern'),

    path('order/<int:pk>/',
         OrderDetail.as_view(),
         name='travelsale_order_detail_urlpattern'),

    path('order/create/',
         OrderCreate.as_view(),
         name='travelsale_order_create_urlpattern'),

    path('order/<int:pk>/update/',
         OrderUpdate.as_view(),
         name='travelsale_order_update_urlpattern'),

    path('order/<int:pk>/delete/',
         OrderDelete.as_view(),
         name='travelsale_order_delete_urlpattern'),

    path('travelproduct/',
         TravelproductList.as_view(),
         name='travelsale_travelproduct_list_urlpattern'),

    path('travelproduct/<int:pk>/',
         TravelproductDetail.as_view(),
         name='travelsale_travelproduct_detail_urlpattern'),

    path('travelproduct/create/',
         TravelproductCreate.as_view(),
         name='travelsale_travelproduct_create_urlpattern'),

    path('travelproduct/<int:pk>/update/',
         TravelproductUpdate.as_view(),
         name='travelsale_travelproduct_update_urlpattern'),

    path('travelproduct/<int:pk>/delete/',
         TravelproductDelete.as_view(),
         name='travelsale_travelproduct_delete_urlpattern'),

    path('type/',
         TypeList.as_view(),
         name='travelsale_type_list_urlpattern'),

    path('type/<int:pk>/',
         TypeDetail.as_view(),
         name='travelsale_type_detail_urlpattern'),

    path('type/create/',
         TypeCreate.as_view(),
         name='travelsale_type_create_urlpattern'),

    path('type/<int:pk>/update/',
         TypeUpdate.as_view(),
         name='travelsale_type_update_urlpattern'),

    path('type/<int:pk>/delete/',
         TypeDelete.as_view(),
         name='travelsale_type_delete_urlpattern'),

    path('destination/',
         DestinationList.as_view(),
         name='travelsale_destination_list_urlpattern'),

    path('destination/<int:pk>/',
         DestinationDetail.as_view(),
         name='travelsale_destination_detail_urlpattern'),

    path('destination/create/',
         DestinationCreate.as_view(),
         name='travelsale_destination_create_urlpattern'),

    path('destination/<int:pk>/update/',
         DestinationUpdate.as_view(),
         name='travelsale_destination_update_urlpattern'),

    path('destination/<int:pk>/delete/',
         DestinationDelete.as_view(),
         name='travelsale_destination_delete_urlpattern'),

    path('customer/',
         CustomerList.as_view(),
         name='travelsale_customer_list_urlpattern'),

    path('student/<int:pk>/',
         CustomerDetail.as_view(),
         name='travelsale_customer_detail_urlpattern'),

    path('student/create/',
         CustomerCreate.as_view(),
         name='travelsale_customer_create_urlpattern'),

    path('student/<int:pk>/update/',
         CustomerUpdate.as_view(),
         name='travelsale_customer_update_urlpattern'),

    path('student/<int:pk>/delete/',
         CustomerDelete.as_view(),
         name='travelsale_customer_delete_urlpattern'),

    path('payment/',
         PaymentList.as_view(),
         name='travelsale_payment_list_urlpattern'),

    path('registration/<int:pk>/',
         PaymentDetail.as_view(),
         name='travelsale_payment_detail_urlpattern'),

    path('registration/create/',
         PaymentCreate.as_view(),
         name='travelsale_payment_create_urlpattern'),

    path('registration/<int:pk>/update/',
         PaymentUpdate.as_view(),
         name='travelsale_payment_update_urlpattern'),

    path('registration/<int:pk>/delete/',
         PaymentDelete.as_view(),
         name='travelsale_payment_delete_urlpattern'),
]
