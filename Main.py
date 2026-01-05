from pyscript import display, document
"""def PON(e)
    document.getElementById('output').innerHTML = " "
    n1=int(document.getElementById('i1').value)
    if n1>0:
        display(f'Number {n1} is a positive number', target="output")
    else:
        display(f'Number {n1} is a negative number', target="output")"""
    
"""def ORE(s):
    document.getElementById('output').innerHTML= " "
    n1=int(document.getElementById('i1').value)
    if n1%2==0:
        display(f'Number {n1} is an even number', target="output")
    else:
        display(f'Number {n1} is an odd number', target="output")"""

def wu(r):
    document.getElementById('output').innerHTML=" "
    w=document.getElementById('i1').value.lower()
    if w == 'raining':
        display(f'Bring an umbrella', target="output")
    else:
        display(f'Wear your sunglasses', target="output")