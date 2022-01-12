# Python Automation

* Install machine agent on Windows
```
# Pre-requisites: python winrm installed
export winrm_endpoint=http://myhost.domain.com:5985/wsman
export domain_username=''
export domain_password=
python install-appd-machine-agent.py
```