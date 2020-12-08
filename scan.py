import json
import os
import time
import requests


"""
virustotal_scan
~~~~~~~~~~~~~~~

Programmatically scan URLs with virustotal.
"""


def scan(url_batch, api_key):
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    scan_id_list = []
    for URL in url_batch:
        try:
            params = {'apikey': api_key, 'url': URL}
            response = requests.post(url, data=params)
            scan_id_list.append(response.json()['scan_id'])
        except ValueError as e:
            print ("Rate limit detected:", e)
            continue
        except Exception:
            print ("Error detected:")
            continue
    return scan_id_list


def report(scan_id_list, api_key):
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    report_list = []
    for id in scan_id_list:
        try:
            params = {'apikey': api_key, 'resource': id}
            response = requests.get(url, params=params)
            report_list.append(response.json())
        except ValueError as e:
            print ("Rate limit detected:", e)
            continue
        except Exception:
            print ("Error detected:")
            continue
    return report_list


def main(link, api_key, output_fp, response_fp):
    print("\n\tESCANEO DE URL")
    url_list = []
    output_file = open(output_fp, 'a')
    response_file = open(response_fp, 'a')
    response = []
    report_list = []
    url_batch = []
    url_batch.append(link)
    response += scan(url_batch, api_key)
    response_file.write('\n'.join(str(t) for t in response))
    print ('Escaneo completo...')

    for i in range(len(response)):
        if i % 4 == 0:
            time.sleep(60)
            scan_list = []
        scan_list.append(response[i])
        if i % 4 == 3 or i == len(response)-1:
            reportBatch = report(scan_list, api_key)
            report_list += reportBatch
            for r in reportBatch:
                json.dump(r, output_file)
                output_file.write("\n")
    output_file.close()
    response_file.close()
