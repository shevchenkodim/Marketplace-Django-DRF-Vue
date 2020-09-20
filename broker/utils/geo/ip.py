from ipware.ip import get_client_ip


def get_client_ip_address(request):
    """ Get ip address from request """
    ip = get_client_ip(request)
    if ip[0]:
        return ip[0]
    else:
        return None
