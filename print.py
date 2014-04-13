from ctypes import *
libc = CDLL("libc.so.6")
message_string = "Do what you love and let it kill you.....!\n"
libc.printf("Charles Browaski: %s", message_string)
