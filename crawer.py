import os
import requests

def save_file(filepath):
    if not os.path.exists(filepath):    
        with open(filepath, 'wb') as fout:
            fout.write(image)

next_offset = -1

while True:
    payload = {'q': 'cat', 'count': 20}
    if next_offset != -1:
        payload['offset'] = next_offset
    try:
        r = requests.get('https://api.cognitive.microsoft.com/bing/v7.0/images/search', payload, headers={'Ocp-Apim-Subscription-Key': '<REPLACE WITH THE ACTUAL KEY>'})
    except:
        print('skipped query')
        next_offset = data['nextOffset']
        total_estimated_matches = data['totalEstimatedMatches']
        if next_offset + 20 > total_estimated_matches:
            break
        continue
    data = r.json()
    for d in data['value']:
        print(d['contentUrl'])
        image_id = d['imageId']
        image_url = d['contentUrl']
        encoding_format = d['encodingFormat']
        try:
            image = requests.get(image_url).content
        except:
            print('skipped image')
            continue
        save_file('./images/cats/{0}.{1}'.format(image_id, encoding_format))
    next_offset = data['nextOffset']
    total_estimated_matches = data['totalEstimatedMatches']
    if next_offset + 20 > total_estimated_matches:
        break

print('Finished!')
