
# Ansible molecule testing for windows:

  

## In windows(remote) machine:

- Run the **UpgradingPowershell&.NET Framework.ps1** powershell script script in the prerequest directory on windows machine's powershell after changing the username and password in that file.

- Now run the **ConfigureRemotingForAnsible.ps1** powershell script script in the same directory on windows machine's powershell.

- check the winrm configuration by using the command

  >winrs -r:'http://localhost:5985/wsman' -u:your_username -p:your_password ipconfig

- Install python which is required for molecule testing.

  

## In linux(host) machine:

- Add the following line to **/etc/hosts** file as

		#windows_machine_ip_address 	host_name

		54.86.64.252 					remote_windows

  
  
  

- Create a **hosts** file inside the playbook's directory as,

		[windows_server]
		remote_windows # host name in **/etc/hosts** file
		
		[windows_server:vars]
		ansible_user=		#Your_username
		ansible_password=	#Your_password
		ansible_connection=winrm
		ansible_winrm_server_cert_validation=ignore

  

- Create a ansible configuration file **ansible.cfg** in same path as,

		[defaults]
		inventory=./hosts
		remote_user=	#Your_username

  

# Reference links

- https://github.com/vipin-k/Ansible-Windows/blob/master/ConfigureRemotingForAnsible.ps1

- https://www.youtube.com/watch?v=SSaEFGlnqYY