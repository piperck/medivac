# coding: utf-8
from fuel.const import DomainName


secret_table = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6",
    "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z",
)


# input parameter is 32bit hex number
def generate_short_url(file_name_hash):
    choise_section = file_name_hash[::2][:12]
    step = len(choise_section)/2

    secret = ''
    for i in xrange(step):
        transform_to_secret = choise_section[i * 2:i * 2 + 2]
        secret += secret_table[int(transform_to_secret, 16) % 62]

    short_url = "%s/%s" % (DomainName.now_domain, secret)

    return short_url
