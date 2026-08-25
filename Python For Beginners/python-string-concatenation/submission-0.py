def concatenate(s1: str, s2: str) -> str:
    s3 = s1 + s2
    msg = "Too long!"

    if len(s3) <= 10:
        return s3
    elif len(s3) > 10:
        return msg




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
