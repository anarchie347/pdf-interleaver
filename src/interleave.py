import pypdf
import sys

firstpath = sys.argv[1]
secpath = sys.argv[2]
savepath = sys.argv[3]
reverse = '-r' in sys.argv[4:]

with open(firstpath, 'rb') as first, open(secpath, 'rb') as second:

    firstpages = pypdf.PdfReader(first).pages
    secpages = pypdf.PdfReader(second).pages
    if reverse:
        secpages = secpages[::-1] # reverse

    firstlen = len(firstpages)
    seclen = len(secpages)


    writer = pypdf.PdfWriter()

    maxlen = max(firstlen, seclen)

    for i in range(0, maxlen):
        if i < firstlen:
            writer.add_page(firstpages[i])
        if i < seclen:
            writer.add_page(secpages[i])





    output = open(savepath, 'wb')
    writer.write(output)
    writer.close()
    output.close()
