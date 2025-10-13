print(
    "valid password"
    if len(passwd := input()) > 8
    and any(ch.isupper() for ch in passwd)
    and any(ch.islower() for ch in passwd)
    and any(ch.isdigit() for ch in passwd)
    and any(not ch.isalnum() and not ch.isspace() for ch in passwd)
    else "invalid password"
)
