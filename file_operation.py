import pdfkit
f = open("sreerag.py", "w")
f.write("print('hai')")
f.close()

with open("sreerag.py" , "r") as f:
    x=f.read()

print(x)

pdfkit.from_url('https://www.w3schools.com/python/python_file_write.asp','shaurya.pdf')