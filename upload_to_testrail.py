import sys
import requests

# TestRail API credentials
testrail_url = 'https://manisha1995narwal.testrail.io'
testrail_user = 'Manisha Narwal'
testrail_password = '064xrIyKiKJ9CGT9c4tl-Gfe9.RuOTTofd.94pFRB'

def upload_results(results_file):
    with open(results_file, 'r') as file:
        results = file.read()

    payload = {
        'status_id': 1,  # Example status ID, adjust as needed
        'comment': results,
    }

    response = requests.post(
        testrail_url,
        auth=(testrail_user, testrail_password),
        json=payload
    )

    if response.status_code == 200:
        print('Results uploaded successfully')
    else:
        print(f'Failed to upload results: {response.status_code}, {response.text}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: upload_to_testrail.py <results_file>')
        sys.exit(1)

    results_file = sys.argv[1]
    upload_results(results_file)
