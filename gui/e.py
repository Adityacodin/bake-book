from cryptography.fernet import Fernet
# from db.database import Database

key = Fernet.generate_key()
# db = Database('localhost', 'KiranMohite', '716807', 'bakery')
# key = Fernet.generate_key()
# db.execute_query("INSERT INTO settings (setting_key,setting_value) VALUES (?,?)",('fernet_key',key.decode()))
print(type(key))
print(key)
print(key.decode())
msg = 'MSG TO be ENCRYPTED'.encode()
f_obj = Fernet(key)
encrypted = f_obj.encrypt(msg)
print(encrypted)

decrypt = f_obj.decrypt(encrypted)
print(decrypt)

s = 'gAAAAABmXybsw27oHIgp4iRyNs34xPi6j4zbImz45Ofb-ntLOawMJyPyTYYerDVny70DvAkMZsYxbqEzRtSPlv-HqWpwS7grY8sTVJdjl30rUjX4cpZ5chU='
print(len(s))


