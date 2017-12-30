import locale
import sys

print(locale.getpreferredencoding())
print(sys.getdefaultencoding())
print(sys.stdin.encoding)
print(sys.stdout.encoding)
print(sys.stderr.encoding)