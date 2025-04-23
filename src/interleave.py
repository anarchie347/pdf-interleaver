import pypdf
import sys

if len(sys.argv) < 2 or sys.argv[1] == '--help' or sys.argv[1] == '-h':
    # Help menu
    print("")
    print("PDF Interleaver")
    print("")
    print("---------------")
    print("")
    print("Takes two PDFs and interleaves the pages")
    print("Intended to combine 2 single-sided scans from a scanner with an auto document feed that doesnt support double sided scans")
    print("")
    print("---------------")
    print("")
    print("Usage:")
    print("python interleave.py first.pdf second.pdf output.pdf [-r]")
    print("")
    print("  -r : reverse the second pdf. Usually needed if the pdfs are from an auto document feed")
    print("")
    print("---------------")
    print("")
    print("Requires:")
    print("python, pypdf library")
    print("")
    print("---------------")
    print("")
    print("Print this page using -h, --help or providing no arguments")
    print("")
    print("---------------")
    print("")
    print("Written and mainted by anarchie347: https://github.com/anarchie347")
    print("Project: https://github.com/anarchie347/pdf-interleaver/")
    print("Issues: https://github.com/anarchie347/pdf-interleaver/issues")
    print("Contribute: https://github.com/anarchie347/pdf-interleaver/pulls")
    print("License: https://github.com/anarchie347/pdf-interleaver/blob/main/LICENSE")
    print("")
    exit()

# Actual program

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
