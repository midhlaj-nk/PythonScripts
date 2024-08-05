import http.client
from codecs import encode
import json

conn = http.client.HTTPSConnection("backend.katootak.com")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'

# vin_number
vin_number = "WP0ZZZ99ZNS257663"  # 17 characters
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name="vin_number"\r\n'))
dataList.append(encode('Content-Type: text/plain\r\n\r\n'))
dataList.append(encode(vin_number))

# license_plate
license_plate = "121"  # 3 characters
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name="license_plate"\r\n'))
dataList.append(encode('Content-Type: text/plain\r\n\r\n'))
dataList.append(encode(license_plate))

# vehicle_data
vehicle_data = {
    "vin": vin_number,
    "vehicle_id": 0,
    "make": "Porsche",
    "model": "911, 911 Carrera, 911 Carrera 4, 911 Carrera S",
    "model_year": 2022,
    "product_type": "Car",
    "body": "Coupe",
    "manufacturer": "DR.ING.H.C. F. PORSCHE AG, D-70435 STUTTGART/ZUFFENHAUSEN",
    "manufacturer_address": "Stuttgart 40, Germany",
    "plant_country": "Germany",
    "engine_manufacturer": "PORSCHE",
    "average_co2_emission_(g/km)": 260.51,
    "number_wheels": 4,
    "number_of_axles": 2,
    "number_of_doors": 2,
    "front_brakes": "Disc",
    "brake_system": "Hydraulic",
    "suspension": "Silencer/Screws",
    "steering_type": "Electric steering",
    "wheel_size": "305/30 ZR21 (100Y)",
    "wheel_size_array": [
        "245/35 ZR20 (91Y)",
        "305/30 ZR21 (100Y)"
    ],
    "wheelbase_(mm)": 2450,
    "wheelbase_array_(mm)": [
        2450
    ],
    "height_(mm)": 1279,
    "length_(mm)": 4519,
    "width_(mm)": 1852,
    "rear_overhang_(mm)": 1062,
    "track_front_(mm)": 1605,
    "track_rear_(mm)": 1567,
    "max_speed_(km/h)": 330,
    "weight_empty_(kg)": 1510,
    "max_weight_(kg)": 1782,
    "max_roof_load_(kg)": 75,
    "abs": 1,
    "check_digit": "Z",
    "sequential_number": "257663"
}
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name="vehicle_data"\r\n'))
dataList.append(encode('Content-Type: application/json\r\n\r\n'))
dataList.append(encode(json.dumps(vehicle_data)))

# closing boundary
dataList.append(encode('--' + boundary + '--'))

# body and payload
body = b'\r\n'.join(dataList)
headers = {
   'Content-type': 'multipart/form-data; boundary={}'.format(boundary) 
}

# send request
conn.request("POST", "/fleet/api/vehicle/", body, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

