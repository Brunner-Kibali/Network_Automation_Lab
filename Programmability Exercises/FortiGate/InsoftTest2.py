import requests
import collections
import pprint

fortigate_user = "admin"
fortigate_password = "admin"


def main(filename='Fortigate'):
    base_url = 'https://192.168.0.122'
    s = requests.Session()

    # Authenticate and obtain cookies, especially APSCOOKIE_ is important for subsequent GET request
    s.post(base_url + "/logincheck", data={"username":fortigate_user, "secretkey":fortigate_password, "ajax":1}, verify=False)

    #PUT
    #/api/v2/cmdb/firewall/address/address1?vdom=root {'subnet': "2.2.2.0
    #255.255.255.0"} #edit firewall address with the specified data


    # PUT /api/v2/cmdb/firewall/address/address1
    # ?vdom=root
    # {"name":"address2"} Rename 'address1' to 'address2',
    #vdom root


    # Using obtained cookies, request for information
    url = base_url + '/api/v2/monitor/system/interface/select/'
    #url = base_url + '/api/v2/monitor/system/admin/select/'




    headers = {'Authorization': f'Bearer {api_token}'}
    params = {'scope': 'global'}

    resp = s.get(url, headers=headers, params=params, verify=False)


    if rep.status_code != 200:
        print(f'Something went wrong. status_code: {rep.status_code}')
        return False

    with open(filename, 'w') as f:
        f.write(resp.text)

    pprint.pprint(resp.json())

    return True

if __name__ == '__main__':
    main()



