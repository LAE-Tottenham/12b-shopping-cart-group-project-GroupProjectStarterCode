from ukpostcodeutils import validation
Postcode = input()
if validation.is_valid_postcode(Postcode):
    print ("Postcode OK.")