from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=255, null=False)
    company_logo = models.CharField(max_length=255, blank=True)  # Can be a URL or file path

    def __str__(self):
        return self.company_name


class IPO(models.Model):
    class IPOStatus(models.TextChoices):
        UPCOMING = 'Upcoming', 'Upcoming'
        OPEN = 'Open', 'Open'
        CLOSED = 'Closed', 'Closed'
        LISTED = 'Listed', 'Listed'

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='ipos')
    price_band = models.CharField(max_length=50, blank=True)
    open_date = models.DateField(null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    issue_size = models.CharField(max_length=100, blank=True)
    issue_type = models.CharField(max_length=50, blank=True)
    listing_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=IPOStatus.choices,
        default=IPOStatus.UPCOMING
    )
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    listing_gain = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    current_market_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_return = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.company.company_name} IPO"


class Document(models.Model):
    ipo = models.ForeignKey(IPO, on_delete=models.CASCADE, related_name='documents')
    rhp_pdf = models.CharField(max_length=255, blank=True)
    drhp_pdf = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Documents for IPO ID {self.ipo.id}"

