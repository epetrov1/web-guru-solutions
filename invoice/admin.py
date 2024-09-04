from io import BytesIO
from django.http import HttpResponse
from django.contrib import admin
from .models import Invoice
from webguru.renderers import render_to_pdf

def generate_and_download_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoices.pdf"'
    
    # Create a buffer to accumulate PDF content
    pdf_buffer = BytesIO()
    
    # Iterate over each selected invoice in the queryset
    for invoice in queryset:
        # Render PDF content for the current invoice
        pdf_content = render_to_pdf('pdfs/invoice.html', {'invoice': invoice})
        
        if pdf_content:
            # Write the PDF content to the buffer
            pdf_buffer.write(pdf_content)
    
    # Get the value of the PDF buffer
    pdf_data = pdf_buffer.getvalue()
    pdf_buffer.close()
    
    # Set the content of the response to the accumulated PDF data
    response.write(pdf_data)
    
    return response

generate_and_download_pdf.short_description = "Generate and Download PDF"

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    readonly_fields = ['invoice_number']  # Make invoice_number non-editable
    actions = [generate_and_download_pdf]  # Add custom admin action
    list_filter = ('created_at', 'company_name',)
