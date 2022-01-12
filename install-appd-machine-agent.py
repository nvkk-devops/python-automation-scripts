import winrm
import os

print('\n********************************\n')
print(os.environ['winrm_endpoint'])
print(os.environ['domain_username'])
print('\n********************************\n')

s = winrm.Session(os.environ['winrm_endpoint'], auth=(os.environ['domain_username'], os.environ['domain_password']), transport='ntlm')

ps_script = """
$machine_agent_url='http://xyz.com/machine-agent/windows/'
$machine_agent_file_name='machineagent-bundle-64bit.zip'
$machine_agent_dest_root='F:/test/'

#### Download machine-agent
$machine_agent_final_url = $machine_agent_url + $machine_agent_file_name
$machine_agent_dest_path = $machine_agent_dest_root + $machine_agent_file_name
$WebClient = New-Object System.Net.WebClient
$WebClient.DownloadFile($machine_agent_final_url, $machine_agent_dest_path)

#### Extract machine-agent
$destination = $machine_agent_dest_root + 'machineagent-bundle-64bit-windows/'
if (!$destination) {
    $destination = [string](Resolve-Path $machine_agent_dest_path)
    $destination = $destination.Substring(0, $destination.LastIndexOf('.'))
    mkdir $destination | Out-Null
}
unzip.exe -o -qq $machine_agent_dest_path -d $destination
Remove-Item $machine_agent_dest_path

#### Re-install machine-agent, Invoke-Expression:notworking
$command_uninstall = $destination + 'UninstallService.vbs'
start cscript.exe $command_uninstall

$command_install = $destination + 'InstallService.vbs'
start cscript.exe $command_install 
"""

r = s.run_ps(ps_script)
print(r.status_code)
print(r.std_out)
print(r.std_err)

print('\n********************************\n')