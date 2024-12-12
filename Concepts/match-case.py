# introduced in python 3.10 
# similar to switch statement in c
# basic syntax: matching statement involves matching a variable against several cases using case keyword. 


def http_status(status):
    match status:
        case 200:
            return "ok"

        case 404:
            return "Page Not Found"

        case _:   # repesents default message/ case
            return "Server Error"

print(http_status(200))
print(http_status(404))
print(http_status(201))