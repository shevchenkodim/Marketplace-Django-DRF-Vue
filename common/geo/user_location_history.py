from django.db import models
from common.geo.geo import CityModel, CountryModel, DistrictModel
from django.conf import settings


class UserLocationHistoryModel(models.Model):
    """ Geo user location history model """
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=20)
    city_id = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    district_id = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
    country_id = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'geo_user_location_history'

    def __str__(self):
        return f'{self.city_id.code}, {self.district_id.code}, {self.country_id.code}'
