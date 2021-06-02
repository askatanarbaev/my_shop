# import braintree
# from django.shortcuts import render, redirect, get_object_or_404
# from orders.models import Order


# def payment_process(request):
#     order_id = request.session.get('order_id')
#     order = get_object_or_404(Order, id=order_id)
#     if request.method == 'POST':
#         # get token for create transacktion
#         nonce = request.POST.get('payment_method_nonce', None)
#         # create and save transaktion
#         result = braintree.Transaktion.sale({
#             'amount':'{:.2f}'.format(order.get_total_cost()),
#             'payment_method_nonce': nonce,
#             'options':{
#                 'submit_for_settlement': True
#             }
#         })
#         if result.is_succes:
#             # chek order as ok
#             order.paid = True
#             # save ID transaktion in order
#             order.braintree_id = result.transaction.id
#             order.save()
#             return redirect('payment:done')
#         else:
#             return redirect('payment:canceled')
#     else:
#         # create one token for JavaSript SDK
#         client_token = braintree.ClientToken.generate()
#         return render(request, 'proccess.html)',{'order': order, 'client_token': client_token})


# def payment_done(request):
#     return render(request, 'payment_done.html')

# def payment_canceled(request):
#     return render(request, 'payment_canceled.html')



import braintree
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        # Получение токена для создания транзакции.
        nonce = request.POST.get('payment_method_nonce', None)
        # Создание и сохранение транзакции.
        result = braintree.Transaction.sale({
        'amount': '{:.2f}'.format(order.get_total_cost()),
        'payment_method_nonce': nonce,
        'options': {
        'submit_for_settlement': True
        }
        })
        if result.is_success:
        # Отметка заказа как оплаченного.
            order.paid = True
            # Сохранение ID транзакции в заказе.
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # Формирование одноразового токена для JavaScript SDK.
        client_token = braintree.ClientToken.generate()
        return render(request,
        'proccess.html',
        {'order': order,
        'client_token': client_token})



def payment_done(request):
    return render(request, 'payment_done.html')

def payment_canceled(request):
    return render(request, 'payment_canceled.html')

