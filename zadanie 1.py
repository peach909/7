Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict_items = { 1: 'a', 2: 'b' } .items()
inv_dict = lambda d: { v: k for k, v in d }
print(inv_dict(dict_items))