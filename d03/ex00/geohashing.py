import sys
from antigravity import geohash
# Geohash: encodes a geographic location into a short string of letters and digits.
# https://docs.quadrant.io/quadrant-geohash-algorithm
# 37.421542 -122.085589 2005-05-26-10458.68
   

def test_geohash():
    if (len(sys.argv) != 4):
        return(print("Wrong Usage!! [geohashing.py <latitude> <longitude> <date>]"))
    try:
        lat = float(sys.argv[1])
    except:
        return print("latitude<float>")
    try:
        long = float(sys.argv[2])
    except:
        return print("longitude<float>")
    try:
        date = sys.argv[3].encode('utf-8')
    except:
        return print("datedow<string>")
    geohash(lat, long, date)


if __name__ == '__main__':
    test_geohash()