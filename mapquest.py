import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "zYpvW1FRRLV8NBlt5j6ETHKM6r8hC9Ss"

while True:
    print("Bienvenidos ")
    orig = input("ciudad de origen: ")
    if orig == "s":
        break
    dest = input("ciudad de destino: ")
    if dest == "s":
        break
    url = main_api + urllib.parse.urlencode({"key":key,"from":orig, "to": dest})
    json_data = requests.get(url).json()

    print("URL:" + (url))
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API status:" + str(json_status) + " = successful route call. \n")
        print("desde: " + (orig) + " hasta: " + (dest))
        print("duracion del viaje: " + (json_data["route"]["formattedTime"]))
        print("kilometros:    " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        #print("combustible(Lts):    " + str(json_data["route"]["fuelused"]*3.78))

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61)+ " Km)"))