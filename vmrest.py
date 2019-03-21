import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
vcip = '10.140.99.89'
s=requests.Session()
s.verify=False
ds = []
ds_name = []
access = []

# Function to get the vCenter server session
def get_vc_session(vcip,username,password):
    s.post('https://'+vcip+'/rest/com/vmware/cis/session',auth=(username,password))
    return s

# Function to get all the VMs from vCenter inventory
def get_ds(vcip, *argv):
    for arg in argv:
        print(arg)
        output_ds=s.get('https://'+vcip+'/rest/vcenter/datastore?filter.names={}'.format(arg))
        data = output_ds.json()
        print(data)
        try:
            ds.append(data['value'][0]['datastore'])
            output_data=s.get('https://'+vcip+'/rest/vcenter/datastore/{}'.format(data['value'][0]['datastore']))
            ds_name.append(data['value'][0]['name'])
            ds_data = output_data.json()
            print(ds_data)

            
            access.append(ds_data['value']['accessible'])
            print(access)
        
            print('Datasore '+arg+' with datastore ID '+data['value'][0]['datastore']+' is still connected')
        except Exception as error:
            # print('DS' + arg + 'Status: '+ error)
            print('Datasore '+arg+' is  disconnected')
    return ds
