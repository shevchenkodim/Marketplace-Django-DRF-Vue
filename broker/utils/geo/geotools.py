from ip2geotools.databases.noncommercial import DbIpCity


def get_location_by_ip(ip_address):
    """ Get location by ip address """
    response = DbIpCity.get(ip_address, api_key='free')
    return response
