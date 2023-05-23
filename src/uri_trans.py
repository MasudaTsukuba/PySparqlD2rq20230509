import re
import requests
import urllib.parse


def uri2str(uri_input):
    return_string = uri_input
    for match in re.finditer(r'<(.*?)>', uri_input):
        match_string = uri_input[match.start():match.end()]
        encoded_url = urllib.parse.quote(match_string, safe=":/?&=")
        # response = requests.get(f'http://localhost:5001/?uri2str={encoded_url}')
        data = {'uri2str': f'{encoded_url}'}
        response = requests.post(f'http://localhost:5001/', json=data)
        if response.status_code == 200:
            data = response.json()
            # print(data['str'])
            if data['str'] != 'null':
                return_string = urllib.parse.unquote(return_string.replace(match_string, data['str']))
        else:
            # print('Error: ', response.status_code)
            pass
    return return_string


def str2uri(str_input):
    return_string = str_input
    # for match in re.finditer(r'http://.*', str_input):
    #     match_string = str_input[match.start():match.end()]
    #     encoded_url = urllib.parse.quote(match_string, safe=":/?&=")
    #     # response = requests.get(f'http://localhost:5001/?str2uri={encoded_url}')
    #     data = {'str2uri': f'{encoded_url}'}
    #     response = requests.post(f'http://localhost:5001', json=data)
    #     if response.status_code == 200:
    #         data = response.json()
    #         # print(data['str'])
    #         return_string = urllib.parse.unquote(return_string.replace(match_string, data['uri']))
    #     else:
    #         # print('Error: ', response.status_code)
    #         pass
    encoded_string = urllib.parse.quote(str_input, safe=":/?&=")
    data = {'str2uri': f'{encoded_string}'}
    print('start request')
    response = requests.post(f'http://localhost:5001', json=data)
    print('end request')
    if response.status_code == 200:
        data = response.json()
        # print(data['str'])
        return_string = urllib.parse.unquote(data['uri'])
    else:
        # print('Error: ', response.status_code)
        pass
    return return_string
