from flask import Flask, request, render_template, redirect
# from controller.twitter import getSearchOptions
majorCities = []

def generateString():
    reqItemString = ""
    print(request.method)
    requiredItems = []
    notRequiredItems = []
    if request.method == "POST":
       # getting input with name = fname in HTML form
       #cityName = request.form.get("cityName")
       # getting input with name = lname in HTML form
       #last_name = request.form.get("Beds")

        cityName = request.form.get("cityName")
        platform = request.form.get("platform")
        beds = request.form.get("bedBox")
        icu = request.form.get("icuBox")
        oxygen = request.form.get("oxygenBox")
        ventilator = request.form.get("ventilatorBox")
        tests = request.form.get("testBox")
        fabiflu = request.form.get("fabifluBox")
        remdesivir = request.form.get("remdesivirBox")
        favipiravir = request.form.get("favipiravirBox")
        tocilizumab = request.form.get("tocilizumabBox")
        plasma = request.form.get("plasmaBox")
        food = request.form.get("foodBox")
        ambulance = request.form.get("ambulanceBox")
        therapy = request.form.get("therapyBox")
        print(cityName, beds, icu, oxygen, ventilator, tests, fabiflu, remdesivir, favipiravir, tocilizumab, plasma, food, ambulance, therapy, platform)
        #return myprints()
        # cityName = "cityName"
        # platform = "platform"
        # beds = "bedBox"
        # icu = "icuBox"
        # oxygen = "oxygenBox"
        # ventilator = "ventilatorBox"
        # tests = "testsBox"
        # fabiflu = "fabifluBox"
        # remdesivir = "remdesivirBox"
        # favipiravir = "favipiravBox"
        # tocilizumab = "tocilizumBox"
        # plasma = "plasmaBox"
        # food = "foodBox"
        # ambulance = "ambulanceBox"
        # therapy = "therapyBox"
        if cityName != '':
            requiredItems.append(cityName)
            if beds == 'beds':
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
        else:
            message="Please add a city name!"
            return render_template("newindex.html",message=message)

        if len(requiredItems)==1:
            message="Please select atleast one resource!"
            return render_template("newindex.html", message=message)
        print(requiredItems)
        if len(requiredItems) != 0:
            reqItemString = "%20".join(requiredItems)

        if platform == 'facebook':
            redirectUrl = "https://www.facebook.com"
        elif platform == 'instagram':
            redirectUrl = "https://www.facebook.com"
        elif platform == 'twitter':
            platformSelection = 'twitter'
            searchOptions= ["All tweets","Only tweets containing 'verified'","Only tweets containing 'unverified'"]
            return render_template("newindex.html", name=platformSelection, searchOptions=searchOptions)
            redirectUrl = "https://www.twitter.com"
            # getSearchOptions(platformSelection)
        else:
            message = "Please select the platform!"
            return render_template("newindex.html",message=message)
        print(reqItemString)

        if len(requiredItems) == 0:
            return render_template("newindex.html")
        else:
            return reqItemString
       #return redirect()
        #Your name is "+first_name + last_name
    return render_template("newindex.html")

def myprints():
    print("somthings")


def extractFromTweet(tweets):
    cityfound = 0
    for city in majorCities:
        for tweet in tweets:
            tweet = tweet.lower()
            if tweet.find(city) != -1:
                cityFound = 1
            if tweet.find("bed") or tweet.find("beds"):
                bedFound = 1
            if tweet.find("oxygen") or tweet.find("oxygens"):
                oxygenFound = 1
            if tweet.find("oxygen") or tweet.find("oxygens"):
                oxygenFound = 1
            if tweet.find("oxygen") or tweet.find("oxygens"):
                oxygenFound = 1
            if tweet.find("oxygen") or tweet.find("oxygens"):
                oxygenFound = 1
