from django.db import models


class Location(models.Model):
    """ Abstract location model """
    code = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True


class CountryModel(Location):
    """ Country model """

    class Meta:
        db_table = 'geo_location_country_code'

    def __str__(self):
        return f'{self.code}'


class DistrictModel(Location):
    """ District model """

    class Meta:
        db_table = 'geo_location_district_code'

    def __str__(self):
        return f'{self.code}'


class CityModel(Location):
    """ City model """

    class Meta:
        db_table = 'geo_location_city_code'

    def __str__(self):
        return f'{self.code}'
