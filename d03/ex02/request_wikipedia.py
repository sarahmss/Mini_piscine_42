import sys
import requests
import dewiki #https://github.com/daddyd/dewiki
import json

# pip install -r requirement.txt
# get() method : sends a GET request to the specified url.
# raise_for_status(): check if an error has occurred
# json.loads():  takes a file object and returns the json object
# JSONDecodeError: indicates there is an issue with the way in which your JSON data is formatted.
# parameters: https://requests.readthedocs.io/en/latest/user/quickstart/

def request_wiki():
    parameters = {
                "action": "parse",
                "page": sys.argv[1],
                "prop" : "wikitext", # page content
                "format" : "json",
                "redirects" : "true"
            }
    try:
        result = requests.get(url="https://en.wikipedia.org/w/api.php", params=parameters)
        result.raise_for_status()
    except requests.HTTPError as exception:
        raise exception
    try:
        json_obj = json.loads(result.text)
    except json.decoder.JSONDecodeError as exception:
        raise exception
    if json_obj.get("error") != None:
        raise Exception(json_obj["error"]["info"])
    return(dewiki.from_string(json_obj["parse"]["wikitext"]["*"]))

   
def request_wikipedia():
    if (len(sys.argv) != 2):
        sys.exit("Wrong Usage [python3 request_wikpedia.py <title>]")
    try:
        wiki_data = request_wiki()
    except Exception as exception:
        print(exception)
    try:
        final_file = open((sys.argv[1].replace(" ", "_") + ".wiki"), 'w')
        final_file.write(wiki_data)
        final_file.close()
    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    request_wikipedia()