cityName = "cityName"
platform = "platform"
beds = "beds"
icu = "icu"
oxygen = "oxygen"
ventilator = "ventilator"
tests = "tests"
fabiflu = "fabiflu"
remdesivir = "remdesivir"
favipiravir = "favipirav"
tocilizumab = "tocilizum"
plasma = "plasma"
food = "food"
ambulance = "ambulance"
therapy = "therapy"

requiredItems = []
if cityName != '':
    requiredItems.append(cityName)
if beds == "beds":
    requiredItems.append(beds)
if icu == 'icu':
    requiredItems.append(icu)
if oxygen == 'oxygen':
    requiredItems.append(oxygen)
if ventilator == 'ventilator':
    requiredItems.append(ventilator)
if tests == 'tests':
    requiredItems.append(tests)
if fabiflu == 'fabiflu':
    requiredItems.append(fabiflu)
if remdesivir == 'remdesivir':
    requiredItems.append(remdesivir)
if favipiravir == 'favipiravir':
    requiredItems.append(favipiravir)
if tocilizumab == 'tocilizumab':
    requiredItems.append(tocilizumab)
if plasma == 'plasma':
    requiredItems.append(plasma)
if food == 'food':
    requiredItems.append(food)
if ambulance == 'ambulance':
    requiredItems.append(ambulance)
if therapy == 'therapy':
    requiredItems.append(therapy)
    
print(requiredItems)
reqItemString = "%20OR%20".join(requiredItems)
# print("shubham")
l = len(reqItemString)
#rItemString = reqItemString[:l-2]
rItemString = "(" +reqItemString +  ")"
print(rItemString)
