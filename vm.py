#Imports
import getpass
import subprocess

# User Input
host=raw_input("What is the hostname? (ex: ql1foo1) > ")
env=raw_input("What environment? (t=TEST, b=BETA, p=PROD) > ")
dc=raw_input("Which data center? (d=DETROIT, t=TROY) > ")
passw=getpass.getpass()

# ENV variables
if env == "t":
	env = "test"
	os = "CentOS-7-x86_64-VM"
	fqdn = ".test.rockfin.com"
elif env == "b":
	env = "beta"
	os = "CentOS-7-x86_64-VM"
	fqdn = ".beta.rockfin.com"
elif env == "p":
	env = "prod"
	os = "RHEL-7-x86_64-VM"
	fqdn = ".prod.rockfin.com"
elif env == 'c':
	env = "corp"
	os = "CentOS-7-x86_64-VM"
	fqdn = ".mi.corp.rockfin.com"
else:
	raise NameError('INVALID ENVIRONMENT')

# DC variables
if dc == "d":
	dc = "detroit"
	vsphere = "ql1vcenter1"
elif dc == "t":
	dc = "troy"
	vcenter = "ql2vcenter1"
else:
	raise NameError('INVALID DATACENTER')

# Verify
print """
Does this look correct?:

	Hostname: %s%s
	OS: %s
	Environment: %s
	Datacenter: %s
	vSphere: %s
	Password: %s
	""" % (host,fqdn,os,env,dc,vcenter,passw)

#subprocess.call("/sashell/spacewalk/systemadd.sh -h " + host + " -p CentOS-7-x86_64-VM --env " + env + " --dc= " + dc, shell=True)
#subprocess.call("/sashell/sbin/vmpoweron.py, shell=True)
#subprocess.call("/sashell/sbin/vmsetvlan.py, shell=True)
