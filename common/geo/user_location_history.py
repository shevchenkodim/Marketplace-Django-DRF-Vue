from django.db import models
from common.geo.geo import CityModel, CountryModel, DistrictModel, IpAddressModel
from django.conf import settings
from broker.utils.geo.ip import get_client_ip_address
from broker.utils.geo.geotools import get_location_by_ip
from common.models import User


class UserLocationHistoryModel(models.Model):
    """ Geo user location history model """
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IpAddressModel, on_delete=models.CASCADE)
    city_id = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    district_id = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
    country_id = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    json_data = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'geo_user_location_history'

    def __str__(self):
        return f'{self.city_id.code}, {self.district_id.code}, {self.country_id.code}'

    @staticmethod
    def create_user_location(request, user_id):
        ip_address = get_client_ip_address(request)
        if ip_address == '127.0.0.1':
            return False
        location = get_location_by_ip(ip_address)
        UserLocationHistoryModel.objects.create(
            user_id=User.objects.get(id=user_id),
            ip_address=IpAddressModel.objects.get_or_create(ip_address=ip_address)[0],
            city_id=CityModel.objects.get_or_create(code=location.city)[0],
            district_id=DistrictModel.objects.get_or_create(code=location.region)[0],
            country_id=CountryModel.objects.get_or_create(code=location.country)[0],
            json_data=location.to_json()
        )
        return True
