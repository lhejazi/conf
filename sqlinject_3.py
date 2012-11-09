import mechanize

br = mechanize.Browser()
br.open("http://ec2-54-245-12-74.us-west-2.compute.amazonaws.com/sqlinject3/")
assert br.viewing_html()

br.select_form(nr=0)
br["myusername"] = "mibailey"
br["mypassword"] = "129581926211651571912466741651878684928"

response = br.submit()

print response.read()
