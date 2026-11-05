data = [
    {
        "name": "Sorna",
        "valid": True
    },
    {
        "name": "Priscilla",
        "valid": True
    },
    {
        "name": "John",
        "valid": False
    },
    {
        "name": "Sarah",
        "valid": False
    }
]

def authenticated(fn):
    def wrap(*args, **kwargs):
        users = args[0] if args else kwargs.get('users', [])
        for user in users:
            if user['valid']:
                fn(user)
            else:
                print(f'{user['name']} is not authenticated')
    return wrap

@authenticated
def message_friends(user):
    print(f"message has been sent to {user["name"]}")

message_friends(data)
