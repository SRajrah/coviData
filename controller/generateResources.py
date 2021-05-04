from flask import Flask, request, render_template, redirect
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
        requirement = request.form.get("requirement")
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
        if platform=='twitter':
            twitterUnverifiedFilter = request.form.get("unverified")
            twitterVerifiedFilter = request.form.get("verified")

        print(cityName,requirement, beds, icu, oxygen, ventilator, tests, fabiflu, remdesivir, favipiravir, tocilizumab, plasma, food, ambulance, therapy, platform, twitterNeedFilter,twitterRequireFilter)
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
        if cityName != 'None':
            if requirement!= 'None':
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
                message="Please select your requirement- You can find or provide resources!"
                return render_template("newindex.html",message=message)
        else:
            message="Please add a city name!"
            return render_template("newindex.html",message=message)
        print(len(requiredItems))
        if len(requiredItems)==2:
            message="Please select atleast one resource!"
            return render_template("newindex.html", message=message)

        # print(requiredItems)
        # if len(requiredItems) != 0:
        #     reqItemString = "%20".join(requiredItems)
        
        if platform == 'facebook':
            if requirement=='need':
                stringToSearch = cityName+" "+(" ").join(requiredItems)+" need"
            redirectUrl = "https://www.facebook.com/search/top?q="+stringToSearch
            return redirect(redirectUrl)
        elif platform == 'instagram':
            redirectUrl = "https://www.facebook.com"
        elif platform == 'twitter':
            platformSelection = 'twitter'
            if requirement=='need':
                if twitterUnverifiedFilter:
                    stringToSearch = twitterUnverifiedFilter+" "+cityName+" ("+(" OR ").join(requiredItems)+") "+"(needed OR need OR required OR require OR needs) "+'-"not verfied" '+'-"unverified"'
                else:
                    stringToSearch = twitterUnverifiedFilter+" "+cityName+" ("+(" OR ").join(requiredItems)+") "+"(needed OR need OR required OR require OR needs) "+'-"not verfied" '+'-"unverified"'

            else:
                stringToSearch = twitterRequireFilter+" "+cityName+" ("+(" OR ").join(requiredItems)+") "+"(available OR present) "+'-"not available" '+'-"not present"'
# /search?q=verified%20Shimla%20(bed%20OR%20beds%20OR%20icu%20OR%20oxygen%20OR%20ventilator%20OR%20ventilators%20OR%20test%20OR%20tests%20OR%20testing)%20-"not%20verified"%20-"unverified"&f=live          
            searchOptions= ["All tweets","Only tweets containing 'verified'","Only tweets containing 'unverified'"]
            # return render_template("newindex.html", name=platformSelection, searchOptions=searchOptions)
            redirectUrl = "https://www.twitter.com/search?q="+stringToSearch
            return redirect(redirectUrl)
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
