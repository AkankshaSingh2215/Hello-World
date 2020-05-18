#email slicer

email = input("what is your email address?").strip() #strip()method removes any leading and trailing characters

#slice out the user name before @
user_name = email[:email.index("@")]

#slice out the domain name after @
domain_name = email[email.index("@")+1:]

#format function allows multiple subsitution and value formatting 
output = "your user name is '{}'and your domain name is'{}'".format(user_name, domain_name)

#display the output
print(output)
