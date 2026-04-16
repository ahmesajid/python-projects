import requests,sys

#city=input("Enter City : ")
city=sys.argv[1]
#TAKES SECOND ARG FROM CONSOLE INPUT 

API_KEY="b821c6b740917ba3bfc841e932771429"
#GEN YOU KEY AND TRY THIS LINK
#url=f"http://api.openweathermap.org/data/2.5/weather?q=Lahore&appid={API_KEY}"
url2=f"https://wttr.in/{city}/?format=j1" #J1 JSON FORMAT

getData=requests.get(url2).json()
getTempData=getData["current_condition"][0]

print( "**************************************************")
print( f"************** WEATHER IN {city.upper()} ***************")
print( "**************************************************")
print(f"Feels like  : {getTempData['FeelsLikeC']}")
print(f"Humidity    : {getTempData['humidity']}")
print(f"Temperature : {getTempData['temp_C']} (deg C)")
print(f"Weather     : {getTempData['weatherDesc'][0]['value']}")
print(f"Wind speed  : {getTempData['windspeedKmph']} kmph")
print( "**************** WEATHER REPORT ******************")
