import facebook
import datetime
import requests
import json
import webbrowser

token = '''EAAOwpskxmYQBAHZCi8To8DRyxA7WLBJZBpT9BSxShRwljh41OePH7FW2Qd0
            qZBkiZCYN2LZCqFdfdU0RX3ug77kmVRkg8qmPsxFHjcevpzgZAJ6kiTZA8S
            Uhuqoh7JLT2lpZAGBOm2sFnPQOhZAdnN1uS8KzIUEUhvU9aQ29E3lLgDUVh2
            WNlK9EerYcpzgl6UOZA7klbmhsUiowByEOwZCG62WLbIvSaPGGZChrGQtB6ZB
            3AlvHkjmYyFXHsOyvQMLiFGMoZD'''
def get_likes_api():
    try:
        graph = facebook.GraphAPI(access_token=token, version=3.1)
        likes =  graph.request('/me/likes')['data']
        user = graph.request('/me?fields=name')
        print(likes)
        print(user)
        newlist = []
    except Exception as e:
        print(e)

if __name__ == "__main__":

    search = "https://www.google.com/search?q=DIY+Resuing+Ideas+for"+results
    webbrowser.open(search)


