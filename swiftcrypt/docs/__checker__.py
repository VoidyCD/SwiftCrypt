import swiftcrypt
import __hash__

password = "551pWS$swdW$#do@$"


"""check_password_strength-args: actual password, the min length, min uppercases, min lowercases, min numbers, min speicals and if messages should be returned."""
strength = swiftCrypt.Checker().check_password_strength(password,min_length=12,min_uppercase=3,min_lowercase=4,min_numbers=2,min_special=2,return_message=False)

"""If return_message is enabled, the function will print what is missing from the password, example: not enough length, or not enough numbers.
if this is disabled, it will only return the password strength. example: 80, 20, 50 / 100
"""

print(strength)
    
password, hashedPass, salt = __hash__.returnHash()

"""verifiedPass-args: actual password, the hashed version, and the salt used aswell as the algorithm.""" 
verifiedPass = swiftCrypt.Checker().verify_password(password, hashedPass, salt,"sha256")
if verifiedPass == True:
    print("Password is correct!")
else:
    print("Password is incorrect!")                             
