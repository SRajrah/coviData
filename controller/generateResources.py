from flask import Flask, request, render_template, redirect
def generateString():
    print(request.method)
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form
       last_name = request.form.get("lname")
       platform = request.form.get("platform")
       #return myprints()
       if platform == 'facebook':
           redirectUrl = "https://www.facebook.com"
       if platform == 'twitter':
           redirectUrl = "https://www.twitter.com"
       if platform == 'instagram':
           redirectUrl = "https://www.instagram.com"

       return redirect(redirectUrl)
        #Your name is "+first_name + last_name
    return render_template("index.html")

def myprints():
    print("somthings")