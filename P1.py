Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello\nWorld")
Hello
World
type(int(1.0))
<class 'int'>
bool(1)
True
# Try your first Python output

... print('Hello, Python Bro!')
Hello, Python Bro!
>>> # Check the Python Version
... 
... import sys
... print(sys.version)
SyntaxError: multiple statements found while compiling a single statement
>>> KeyboardInterrupt
>>> # Check the Python Version
... 
... import sysprint(sys.version)
SyntaxError: invalid syntax
>>> # Check the Python Version
... import sys
>>> print(sys.version)
3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]
>>> 3 + 2 * 2
7
>>> name = 'Lizz'
>>> print(name[0:2])
Li
>>> var = '01234567'
>>> print(var[::2])
0246
>>> '1'+'2'
'12'
>>> myvar = 'hello'
>>> print(upper(myvar))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(upper(myvar))
NameError: name 'upper' is not defined. Did you mean: 'super'?
>>> print(Upper(myvar))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(Upper(myvar))
NameError: name 'Upper' is not defined. Did you mean: 'super'?
>>> print(myvar.upper())
HELLO
