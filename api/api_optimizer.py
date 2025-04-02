import redis
import fetch_osint
import json

cache = redis.Redis(host="localhost", port=6379, db=0)

def get_threat_data(ip):
    cached_data = cache.get(ip)
    if cached_data:
        return cached_data.decode("utf-8") #decode data as string
    else:
        data = fetch_osint.fetch_osint_updates(ip) #call Ip if not cached
        if data is not None:
            # Only set cache if data is valid
            cache.setex(ip, 3600, data) 
            return data #return the data
        else:
            #log and retrun message if no data is found
            print(f"Skipping cache for IP {ip}, no data found.")
            return None #return No if no

ip = fetch_osint.IP_ADDRESS

print(get_threat_data(ip))
