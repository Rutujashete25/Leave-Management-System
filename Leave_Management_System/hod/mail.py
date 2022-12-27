# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string


# def staff_detail_mail():
#     context = {
#         'order':order,
#         'payment':payment,
#     }
#     html_body = render_to_string("products/orderplaced_temp.html", context)

#     message = EmailMultiAlternatives(
#         subject='Eshopper Order Details',
#         body=f'Hi, click on this link to check your status  http://127.0.0.1:8000/products/Tracking_Order/ ',
#         from_email='sohailbadeghar561@gmail.com',
#         to=[eamil]
#         )
#     message.attach_alternative(html_body, "text/html")
#     message.send(fail_silently=False