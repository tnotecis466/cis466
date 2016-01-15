import json

import helpers
import requests


# IPv4 VirusTotal function for passive DNS


def vt_ipv4_lookup(ipv4):
    try:
        con = libs.helpers.db_connection()
        with con:
            cur = con.cursor()
            cur.execute("SELECT apikey from settings")
            apikey = cur.fetchall()
            apikey = str(apikey[0][0])
        url = "https://www.virustotal.com/vtapi/v2/ip-address/report"
        params = {'ip': ipv4, 'apikey': apikey}
        r = requests.get(url, params=params, verify=False, proxies=libs.helpers.get_proxy())
        j = json.loads(r.text)
        j['resolutions'] = sorted(j['resolutions'], key=lambda k: k['last_resolved'], reverse=True)
        return j
    except:
        pass


# Domain VirusTotal function for passive DNS
def vt_domain_lookup(domain):
    try:
        con = libs.helpers.db_connection()
        with con:
            cur = con.cursor()
            cur.execute("SELECT apikey from settings")
            apikey = cur.fetchall()
            apikey = str(apikey[0][0])
        url = "https://www.virustotal.com/vtapi/v2/domain/report"
        params = {'domain': domain, 'apikey': apikey}
        r = requests.get(url, params=params, verify=False, proxies=libs.helpers.get_proxy())
        j = json.loads(r.text)
        j['resolutions'] = sorted(j['resolutions'], key=lambda k: k['last_resolved'], reverse=True)
        if len(j) < 20:
            pass
        else:
            return j
    except:
        pass


def vt_hash_lookup(filehash):
    try:
        con = libs.helpers.db_connection()
        with con:
            cur = con.cursor()
            cur.execute("SELECT apikey from settings")
            apikey = cur.fetchall()
            apikey = str(apikey[0][0])
        url = "https://www.virustotal.com/vtapi/v2/file/report"
        params = {'resource': filehash, 'apikey': apikey}
        r = requests.get(url, params=params, verify=False, proxies=libs.helpers.get_proxy())
        j = json.loads(r.text)
        return j
    except:
        pass
