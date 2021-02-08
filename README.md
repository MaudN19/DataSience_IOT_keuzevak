# IOT_keuzevak_Luchtvochtigheid
Het doel vandit project ligt bij mij vooral bij kennis opdoen in het project zodat ik dit later kan gebruiken. De kennis die ik heb opgedaan in mijn project wil ik meenemen om in het vervolg mijn eigen IOT project te kunnnen opzetten en deze kunnen uitwerken.

# Probleem en Doelstelling
Het probleem dat ik wil gaan oplossen is het aangeven van wanneer moet het raam open komen te staan om de luchtvochtigheid op mijn kamer te gaan verbeteren. Het probleem op de kamer vooral te maken dat de kamer op de zolder is en deze de warme droge lucht van het huis zich verzamelt. Hierdoor wordt het zeer vervelend om de kamer te verblijven. De doelstelling van mijn project is om de luchtvochtigheid op de kamer te kunnen monitoren en helpen verbeteren door te kijken wanneer het raam open te zetten helpt om de luchtvochtigheid te kunnen verbeteren in de kamer.

# Benodigde onderdelen
voor de setup van de het project. Is er gebruik gemaakt van de volgende onderdelen
  1. DockerPI SensorHub
  2. Externe tempratuur sensor
  3. raspberry Pi (gebruikt is een Pi3 model B+)

# De visualisatie van data
Voor het visualiseren van de verzonden data is er gebruik gemaakt van thingspeak. Op thingspeak wordt de data in een grafiek weer gegeven, zodat deze overzichtelijk te zien is. dit zal ook een beter beeld geven in plaats van een lijst. De 4 gemten waarden: Tempratuur, Luchtdruk, Barometer Tempratuur en Barometer luchtdruk. Zijn in 4 apparte grafieken uitgezt om het overzichtlijk te maken voor de gebruiker.

# Proces
Voordat dat ik bij de eindversie van het prototype was gekomen, zijn er meerdere versies geweest. In de eerste 2 versies van het project werkte het versturen van de data vanaf de raspberry pi naar thingspeak niet, dit kwam uiteindelijk doordat de senor geen bestand aanmaakte waarin data werd opgeslagen, in plaats daarvan gaf de sensor de data weer en verwijderde het vervolgens als deze weer opnieuw begon. 

# Bronnen en inspiratie voor de geschreven code
De geschreven code is een combinatie van de twee bronnen met aanpassingen om de code werkend te krijgen. De bronnen die gebruikt zijn voor het schrijven zijn de onderstaande 2 bronen.
https://github.com/notenoughtech/NodeRED-PRojects/blob/master/DockerPi%20Sensor%20Board/SensorBoard_script.py
https://iotdesignpro.com/projects/how-to-send-data-to-thingspeak-cloud-using-raspberry-pi

