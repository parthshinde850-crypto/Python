def http_status(status):
    match status:
        case 200:
            return "OK"
        
    match status:
        case 404:
            return "Not Found"

    match status:
        case 500:
            return "Internal Server error"

    match status:
        case _:
            return "Unknown Status"

print(http_status(200)) 
print(http_status(404)) 
print(http_status(500)) 
print(http_status(100)) 