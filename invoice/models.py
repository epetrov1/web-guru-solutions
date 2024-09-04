from django.db import models

class Invoice(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    eik = models.IntegerField(default=0, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    invoice_number = models.CharField(max_length=20, unique=True, editable=False)
    single_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    product_description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.invoice_number}"

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set invoice_number for new instances
            last_invoice = Invoice.objects.order_by('-id').first()
            if last_invoice:
                last_number = int(last_invoice.invoice_number)
            else:
                last_number = 0
            self.invoice_number = str(last_number + 1).zfill(10)  # Format invoice_number
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        ordering = ['-created_at']