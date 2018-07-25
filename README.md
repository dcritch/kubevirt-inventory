# kubevirt-inventory
An [ansible](https://www.ansible.com/) dynamic inventory script for kubevirt.

## usage

This inventory relies on environment variables to work properly. Before calling the script, export the kubevirt endpoint and token. Optionally, a project/namespace can be specified. If no namespace is set, the script will return a list of all virtual machine instances in the cluster.

~~~
# export OPENSHIFT_TOKEN=$(oc whoami -t)
# export OPENSHIFT_ENDPOINT=$(oc config view | awk '/server/ {print $2}')
# ./kubevirt-inventory.py
{   
    "vmuser1": {
        "hosts": [
            "10.129.0.39",
            "10.129.0.40",
            "10.129.0.41",
            "10.129.0.44"
        ]
    },
    "vmuser2": {
        "hosts": [
            "10.129.0.42",
            "10.129.0.43",
            "10.129.0.45",
            "10.129.0.46"
        ]
    },
    "vmuser3": {
        "hosts": [
            "10.129.0.48",
            "10.129.0.49",
            "10.129.0.47",
            "10.129.0.50"
        ]
    }
}
# ansible -i kubevirt-inventory.py -m ping all
10.129.0.44 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.39 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.40 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.41 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.48 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.49 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.42 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.47 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.43 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.50 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.45 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.46 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
~~~

With a namespace set:

~~~
# export OPENSHIFT_TOKEN=$(oc whoami -t)
# export OPENSHIFT_ENDPOINT=$(oc config view | awk '/server/ {print $2}')
# export OPENSHIFT_NAMESPACE='vmuser1'
# ansible -i kubevirt-inventory.py -m ping all
10.129.0.39 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.44 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.41 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
10.129.0.40 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
~~~



