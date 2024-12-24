



from idmlib import idmManager 

file_path = 'test.vidm'
idm = idmManager(file_path, save_in_appdata=False)
print(idm.get_content('msg')) 


idm.set_language('ex2')
print(idm.get_content('msg'))  

