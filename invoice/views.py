from io import BytesIO
from django.shortcuts import render
from django.http import Http404
from django.core.mail import EmailMessage
from django.template.loader import get_template
from xhtml2pdf import pisa
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from invoice.serializers import InvoiceSerializer



class InvoiceView(APIView):

    def post(self, request, format=None):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            invoice = serializer.save()
            pdf_content = generate_invoice_pdf(serializer.validated_data)  
            if pdf_content:
                recipient_email = serializer.validated_data.get('email')
                message = invoice.product_description
                # Send email with invoice attachment
                send_invoice_email(recipient_email, message, pdf_content)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def generate_invoice_pdf(invoice):
    template_path = 'pdfs/invoice.html'
    context = {'invoice': invoice}
    
    template = get_template(template_path)
    html = template.render(context)
    
    pdf_buffer = BytesIO()
    font_config = {
        'font_path': 'https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap',
        'css': 'body { font-family: "Roboto", sans-serif; }'
    }
    
    try:
        # Generate PDF from HTML
        pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf_buffer, encoding="UTF-8", **font_config)
        return pdf_buffer.getvalue()
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
        return None

def send_invoice_email(recipient_email, message, pdf_content):
    subject = 'Поръчка за абонамент'
    message = message
    from_email = 'info@slflearner.com'
    
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=from_email,
        to=[recipient_email]
    )

    # Attach the PDF content to the email
    email.attach('invoice.pdf', pdf_content, 'application/pdf')

    try:
        # Send the email
        email.send()
        print("Email sent successfully.")
        print(email.attach)
    except Exception as e:
        print(f"Error sending email: {str(e)}")