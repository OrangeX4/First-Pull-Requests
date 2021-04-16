import re
import sys
import pathlib

r = re.compile(
    r"<!\-\- BEGIN:TAG \-\->.*<!\-\- END:TAG \-\->", 
    re.DOTALL
)

chunk = "<!-- BEGIN:TAG -->\n{}\n<!-- END:TAG -->".format(sys.argv[1])

root = pathlib.Path(__file__).parent.resolve()
readme = root/"README.md"

rewritten = readme.open().read()
rewritten = r.sub(chunk, rewritten)

readme.open("w").write(rewritten)
