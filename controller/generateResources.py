from flask import Flask, request, render_template, redirect

majorCities = []

def usefulLinks():
    return  render_template("UsefulLinks.html")

def donationLinks():
    return  render_template("donationLinks.html")

def generateString():
    reqItemString = ""

    requiredItems = []

    if request.method == "POST":
        #get form data into variables
        cityName = request.form.get("cityName")
        cityName = cityName.strip()
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

        print(cityName, requirement, beds, icu, oxygen, ventilator, tests, fabiflu, remdesivir, favipiravir, tocilizumab, plasma, food, ambulance, therapy, platform)

        if cityName is not None:
            if requirement is not None:
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
                message = "Please select your requirement- You can find or provide resources!"
                return render_template("newindex.html", message=message)
        else:
            message = "Please add a city name!"
            return render_template("newindex.html", message=message)
        print(len(requiredItems))
        if len(requiredItems) == 0:
            message = "Please select atleast one resource!"
            return render_template("newindex.html", message=message)


        
        if platform == 'facebook':

            if requirement == 'need':
                stringToSearch = cityName + " " + (" ").join(requiredItems) + " available present"
            else:
                stringToSearch = cityName + " " + (" ").join(requiredItems) + " need required"
            redirectUrl = "https://www.facebook.com/search/top?q=" + stringToSearch

            return redirect(redirectUrl)


        elif platform == 'twitter':

            # get unverified and verified values in variables
            twitterUnverifiedFilter = request.form.get("unverified")
            twitterVerifiedFilter = request.form.get("verified")

            if requirement == 'need':
                print(twitterUnverifiedFilter)
                print(twitterVerifiedFilter)
                if twitterUnverifiedFilter is not None and twitterVerifiedFilter is not None:
                    stringToSearch = "("+twitterVerifiedFilter+" OR "+twitterUnverifiedFilter+") "+cityName+" ("+(" OR ").join(requiredItems)+") "+"(available OR present) "+'-"needed"'+'-"need" '+'-"required" '+'-"require" '+'-"needs" '

                elif twitterUnverifiedFilter is not None and twitterVerifiedFilter is None:
                    stringToSearch = twitterUnverifiedFilter+" "+cityName+" ("+(" OR ").join(requiredItems)+") "+"(available OR present) "+'-"needed"'+'-"need" '+'-"required" '+'-"require" '+'-"needs" '

                elif twitterUnverifiedFilter is None and twitterVerifiedFilter is not None:
                    stringToSearch = twitterVerifiedFilter+" "+cityName+" ("+(" OR ").join(requiredItems)+") "+"(available OR present) "+'-"needed"'+'-"need" '+'-"required" '+'-"require" '+'-"needs" '
                else:
                    stringToSearch = cityName+" ("+(" OR ").join(requiredItems)+") "+"(available OR present) "+'-"needed"'+'-"need" '+'-"required" '+'-"require" '+'-"needs" '

            else:

                if twitterUnverifiedFilter is not None and twitterVerifiedFilter is not None:
                    stringToSearch = twitterVerifiedFilter+" "+twitterUnverifiedFilter+" "+cityName+" ("+(" OR ").join(requiredItems)+") "+"(needed OR need OR required OR require OR needs OR patient OR patients) "+'-"available" '+'-"present"'

                elif twitterUnverifiedFilter is not None and twitterVerifiedFilter is None:
                    stringToSearch = twitterUnverifiedFilter+" "+cityName+" ("+(" OR ").join(requiredItems)+") "+"(needed OR need OR required OR require OR needs OR patient OR patients) "+'-"available" '+'-"present"'

                elif twitterUnverifiedFilter is None and twitterVerifiedFilter is not None:
                    stringToSearch = twitterVerifiedFilter+" "+cityName+" ("+(" OR ").join(requiredItems)+") "+"(needed OR need OR required OR require OR needs OR patient OR patients) "+'-"available" '+'-"present"'
                else:
                    stringToSearch = cityName+" ("+(" OR ").join(requiredItems)+") "+"(needed OR need OR required OR require OR needs OR patient OR patients) "+'-"available" '+'-"present"'


            redirectUrl = "https://www.twitter.com/search?q="+stringToSearch
            return redirect(redirectUrl)
        else:
            message = "Please select the platform!"
            return render_template("newindex.html",message=message)
        print(reqItemString)

        if len(requiredItems) == 0:
            return render_template("newindex.html")
        else:
            return reqItemString

    return render_template("newindex.html")
