import geoip2.database

reader = geoip2.database.Reader("data/GeoLite2-City.mmdb")

def get_ip_location(ip):
    try:
        response = reader.city(ip)
        city = response.city.name or "Unknown City"
        country = response.country.name or "Unknown Country"
        return f"{city}, {country}"
    except:
        return "Unknown Location"
