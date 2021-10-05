import pywhatkit
pywhatkit.text_to_handwriting('''This Is A sample Text 
To Use Mutiline Text you must use triple quotes or it will give a error
0. first install this module using \'pip install pywhatkit.\'
1. this is quite helpful
2. the hndwriting is not good but clear.
3. this work fine with .jpg and .png format.
4. If your text is too long the file may get corrupted.
''',save_to='mytext.png',rgb=(0,0,255))
