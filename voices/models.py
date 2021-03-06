from django.db import models
from dashboard.models import Organization, UserProfile

class Request(models.Model):
    requestDate = models.DateTimeField(auto_now_add=True)
    request1 = models.CharField(max_length=100)
    request2 = models.CharField(max_length=100, default="", null=True, blank=True)
    request3 = models.CharField(max_length=100, default="", null=True, blank=True)
    why1 = models.CharField(max_length=200, default="", null=True, blank=True)
    why2 = models.CharField(max_length=200, default="", null=True, blank=True)
    why3 = models.CharField(max_length=200, default="", null=True, blank=True)
    satisfaction = models.CharField(max_length=50, default="", null=True, blank=True)
    additionalItems = models.CharField(max_length=400, default="", null=True, blank=True)
    ethnicity = models.CharField(max_length=50, default="", null=True, blank=True)
    zipcode = models.CharField(max_length=6, default="", null=True, blank=True)
    birthday = models.CharField(max_length=50, default="", null=True, blank=True)
    gender = models.CharField(max_length=20, default="", null=True, blank=True)
    diet = models.CharField(max_length=100, default="", null=True, blank=True)
    religiousDiet = models.CharField(max_length=100, default="", null=True, blank=True)
    organization = models.ForeignKey(Organization, related_name = 'requests')



    def __str__(self):
        return (str(self.requestDate.strftime('%Y-%m-%d %H:%M:%S')) + ' - ' + self.request1 + ' - ' + 
            self.request2 + ' - ' + self.request3 + ' - ' + self.why1 + ' - ' + self.why2 + ' - ' + 
            self.why3 + ' - ' + self.satisfaction + ' - ' + self.additionalItems + ' - ' + 
            self.ethnicity + ' - ' + self.zipcode + ' - ' + self.birthday + ' - ' + self.gender + ' - ' + 
            self.diet + ' - ' + self.religiousDiet)



class Product(models.Model):
    name = models.CharField(max_length=100)
    prod_type_choices = (
        ('FP', 'Fresh Produce'),
        ('CS', 'Canned Goods & Soup'),
        ('BM', 'Boxed Meals'),
        ('GR', 'Grains, Rice, Beans'),
        ('HE', 'Household Essentials'),
        ('CL', 'Clothing'),
        ('O', 'Others')
    )
    product_type = models.CharField(max_length=2, choices = prod_type_choices)
    picture = models.ImageField(upload_to='photos/product', blank=True, null=True)
    organization = models.ForeignKey(Organization, related_name = 'products')
    quantity = models.IntegerField(default = 0)
    numDonated = models.IntegerField(default = 0)

    def __unicode__(self):
        return (self.name + ' - ' + self.product_type + ' - org: ' + 
            self.organization.name + ' - ' + self.quantity + ' - ' + self.numDonated)

    def __str__(self):
        return (self.name + ' - ' + self.product_type + ' - org: ' + 
            self.organization.name + ' - ' + str(self.quantity) + ' - ' + str(self.numDonated))


# class Products(models.Model):
#     prodName = models.CharField(max_length=100, default=None, blank=True, null=True)
#     prodImg = models.CharField(max_length=400, default=None, blank=True, null=True)
#     prodType = models.CharField(max_length=400, default=None, blank=True, null=True)    

#     def __str__(self):
#         return self.prodName + ' - ' + str(self.prodType)



class Donation(models.Model):
    donationDate = models.DateTimeField(auto_now_add=True)
    donationName = models.CharField(max_length=50, default=None, blank=True, null=True)
    organization = models.ForeignKey(Organization, related_name = 'donations')
    orderNum = models.CharField(max_length=30, default=None, blank=True, null=True)
    quantity = models.IntegerField()
    donor = models.ForeignKey(UserProfile, related_name = 'donations1')


    def __str__(self):
        return (str(self.donationDate.strftime('%Y-%m-%d %H:%M:%S'))  + ' - ' + 
                self.donationName + ' - ' + self.orderNum + ' - ' + 
                str(self.quantity) + ' - ' + self.donor.username) 

