"""Practicing getting information from the website based on the images in my phone"""
#second photo




"""
#first photo
@retry(max_attempts=5, delay=0.5)#this decorator will retry the function 5 times with a delay of 0.5 seconds between each attempt
def fetch_byui_homepage():
    #Fetches the homepage of byui.edu using the request library
    url="http://www.byui.edu"
    response = requests.get(url, timeout=5)
    #raise an exeption if the status code is not successful
    if response.status_code != 200:
        raise ValueError(f"Unable to fetch the homepage of byui.edu. Status code: {response.status_code}")
    return response.text
"""