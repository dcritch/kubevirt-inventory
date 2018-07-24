#!/usr/bin/env python

import requests
import argparse
import json
import os

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("-l","--list", help="list all VM instances in inventory", action="store_true")
  parser.add_argument("--host", help="retrieve variables for <hostname>")
  args = parser.parse_args()

def list_vmis():
  endpoint = os.getenv('OPENSHIFT_ENDPOINT', None)
  namespace = os.getenv('OPENSHIFT_NAMESPACE', None)
  token = os.getenv('OPENSHIFT_TOKEN', None)

  headers = {
    'Authorization': 'Bearer ' + token,
  }

  if namespace is None:
    url = endpoint + '/apis/kubevirt.io/v1alpha2/virtualmachineinstances/'
  else:
    url = endpoint + '/apis/kubevirt.io/v1alpha2/namespaces/' + namespace + '/virtualmachineinstances/'
  vmi_request = requests.get(url, verify=False, headers=headers)
  vmis = vmi_request.json()

  inventory = {}
  for vmi in vmis['items']:
    vmi_namespace = vmi['metadata']['namespace']
    if vmi_namespace not in inventory:
      inventory[vmi_namespace] = {'hosts': []}
    if 'interfaces' in vmi['status']:
      inventory[vmi_namespace]['hosts'].append(vmi['status']['interfaces'][0]['ipAddress'])

  print(json.dumps(inventory, indent=4, sort_keys=True))
  

  #print(json.dumps(vmis, indent=4, sort_keys=True))


if __name__ == '__main__':
  parse_args()
  list_vmis()

