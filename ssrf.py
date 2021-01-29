from requests import get
from sys import argv
from urllib3 import disable_warnings

def do_Request(url, host_header):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                "Host": host_header}
    url_params = {"fromUrlTarget": url}

    try:
        response = get(url, params=url_params, headers=headers, verify=False)
        print('[*] Request sent to: {} || Check your Burp Collaborator TAB [*]'.format(url))

        if('Burp Collaborator'.lower() in response.headers['Server'].lower()):
            print('[+] {} loaded Burp Collaborator Response || Body: {}'.format(url, response.text))

    except Exception as e:
        print('[-] Error on {} !! Stack: {}'.format(url, e))

def main():
    disable_warnings()

    DOMAINS = argv[1]
    BURP_COLLABORATOR = argv[2]

    with open(DOMAINS, 'r') as all_domains:
        for domain in all_domains.readlines():
            domain = domain.replace('\n', '')
            do_Request(domain, BURP_COLLABORATOR)

if __name__ == "__main__":
    main()