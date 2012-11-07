import re
import mechanize

br = mechanize.Browser()
br.open("http://ec2-54-245-12-74.us-west-2.compute.amazonaws.com/sqlinject1/login?came_from=http%3A%2F%2Fec2-54-245-12-74.us-west-2.compute.amazonaws.com%2Fsqlinject1%2F")
# follow second link with element text matching regular expression
#response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
assert br.viewing_html()

br.select_form(nr=0)
# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm.
br["login"] = "mibailey\'; --" # (the method here is
# Submit current form. Browser calls .close() on the current response on
# navigation, so this closes response1
response2 = br.submit()
br.select_form(nr=0)
# print currently selected form (don't call .submit() on this, use br.submit())
print br.form

br["uniqname"] = "nastrein"
br["project"] = ["project1"]
print br["project"]



"""
response3 = br.back() # back to cheese shop (same data as response1)
# the history mechanism returns cached response objects
# we can still use the response, even though it was .close()d
response3.get_data() # like .seek(0) followed by .read()
response4 = br.reload() # fetches from server

for form in br.forms():
		print form
		# .links() optionally accepts the keyword args of .follow_/.find_link()
		for link in br.links(url_regex="python.org"):
		print link
		br.follow_link(link) # takes EITHER Link instance OR keyword args
		br.back()
		"""
