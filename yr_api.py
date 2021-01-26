from yr.libyr import Yr

weather = Yr(location_name="Norway/Trøndelag/Trondheim/Trondheim")
now = weather.now(as_json=True)

print(now)