# The link of the pages consist of 3 parts. 
# first part before the first dot is called subdomain
# last part after the second dot is called top level domain name (TLD)
# mid part(in between the dots) is called domain name.

# www.techtorialacademy.com



# Ask user to enter their website link. 
# Assume that subdomain name will be www and tld will be com
# Print the domain name of the user's website link. 

# Since we know string given will be starting with www. 
# and ending with .com. I need what is in between.

link = input("Please enter the link of your page: ")
domain_name = link.removeprefix("www.").removesuffix(".com")

print(f'The domain name of your page is {domain_name}')