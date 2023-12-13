# As breadcrumb menùs are quite popular today, I won't digress much on explaining them,
# leaving the wiki link to do all the dirty work in my place.
#
# What might not be so trivial is instead to get a decent breadcrumb from your current url.
# For this kata, your purpose is to create a function that takes a url, strips the
# first part (labelling it always HOME) and then builds it making each element but
# the last a <a> element linking to the relevant path; last has to be a <span> element getting the active class.
#
# All elements need to be turned to uppercase and separated by a separator,
# given as the second parameter of the function; the last element can terminate
# in some common extension like .html, .htm, .php or .asp; if the name of the last element
# is index.something, you treat it as if it wasn't there, sending users automatically to the upper level folder.
#
# A few examples can be more helpful than thousands of words of explanation, so here you have them:
#
# generate_bc("mysite.com/pictures/holidays.html", " : ") == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
# generate_bc("www.codewars.com/users/GiacomoSorbi", " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
# generate_bc("www.microsoft.com/docs/index.htm", " * ") == '<a href="/">HOME</a> * <span class="active">DOCS</span>'
# Seems easy enough?
#
# Well, probably not so much, but we have one last extra rule: if one element (other than the root/home)
# is longer than 30 characters, you have to shorten it, acronymizing it (i.e.: taking just the initials
# of every word); url will be always given in the format this-is-an-element-of-the-url and you should
# ignore words in this array while acronymizing:
# ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"];
# a url composed of more words separated by - and equal or less than 30 characters long needs
# to be just uppercased with hyphens replaced by spaces.
#
# Ignore anchors (www.url.com#lameAnchorExample) and parameters
# (www.url.com?codewars=rocks&pippi=rocksToo) when present.
#
# Examples:
#
# generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm", " > ") == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
# generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ") == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'
# You will always be provided valid url to webpages in common formats, so you probably shouldn't
# bother validating them.
#
# If you like to test yourself with actual work/interview related kata, please also consider
# this one about building a string filter for Angular.js.
#
# Special thanks to the colleague that, seeing my code and commenting that I worked on that
# as if it was I was on CodeWars, made me realize that it could be indeed a good idea for a kata :)
import re

def process_part(part: str) -> str:
    skip_list = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]
    if len(part) <= 30:
        part = part.replace("-", " ").upper()
    else:
        part = "".join(token[0].upper() for token in part.split("-") if token not in skip_list)
    return part


def generate_bc(url: str, separator: str) -> str:
    url = re.sub(r'^https?://', "", url, re.I)

    bc_menu = ['<a href="/">HOME</a>']

    hrefs = '<a href="%PATH%">%NAME%</a>'
    span = '<span class="active">%NAME%</span>'
    rel_path = "/"

    parts = url.split('/')[1:]
    if not parts or not parts[0]:
        return '<span class="active">HOME</span>'

    if parts[-1].startswith("index."):
        parts.pop(-1)
    if not parts:
        return '<span class="active">HOME</span>'

    for part in parts[:-1]:
        name = process_part(part)
        rel_path += part + "/"
        bc_menu.append(hrefs.replace("%PATH%", rel_path)
                       .replace("%NAME%", name))
    part = re.match(r'^[a-zA-Z \-]+', parts[-1])
    if part:
        name = process_part(part.group())
        bc_menu.append(span.replace("%NAME%", name))

    return separator.join(bc_menu)

print(generate_bc('https://www.codewars.com#offers', "*"))
assert generate_bc('www.agcpartners.co.uk/', "*") == '<span class="active">HOME</span>'
assert generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm", " > ") == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
assert generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ") == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'
assert generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
assert generate_bc("https://twitter.de/most-viewed/most-viewed/profiles/giacomo-sorbi.html?favourite=code", " * ") == '<a href="/">HOME</a> * <a href="/most-viewed/">MOST VIEWED</a> * <a href="/most-viewed/most-viewed/">MOST VIEWED</a> * <a href="/most-viewed/most-viewed/profiles/">PROFILES</a> * <span class="active">GIACOMO SORBI</span>'
assert generate_bc("https://codewars.com/profiles/pictures-you-wished-you-never-saw-but-you-cannot-unsee-now/pippi-or-uber-bed-immunity-surfer-with-meningitis/by-diplomatic-pippi-and-transmutation-to-from-to/index.php", " - ") == '<a href="/">HOME</a> - <a href="/profiles/">PROFILES</a> - <a href="/profiles/pictures-you-wished-you-never-saw-but-you-cannot-unsee-now/">PYWYNSBYCUN</a> - <a href="/profiles/pictures-you-wished-you-never-saw-but-you-cannot-unsee-now/pippi-or-uber-bed-immunity-surfer-with-meningitis/">PUBISM</a> - <span class="active">DPT</span>'
assert generate_bc("http://www.facebook.fr/eurasian-from-paper-immunity-transmutation/pictures-you-wished-you-never-saw-but-you-cannot-unsee-now/transmutation-immunity-uber-surfer/the-skin-research-at-or-kamehameha-bladder-with-research#team", " : ") == '<a href="/">HOME</a> : <a href="/eurasian-from-paper-immunity-transmutation/">EPIT</a> : <a href="/eurasian-from-paper-immunity-transmutation/pictures-you-wished-you-never-saw-but-you-cannot-unsee-now/">PYWYNSBYCUN</a> : <a href="/eurasian-from-paper-immunity-transmutation/pictures-you-wished-you-never-saw-but-you-cannot-unsee-now/transmutation-immunity-uber-surfer/">TIUS</a> : <span class="active">SRKBR</span>'

