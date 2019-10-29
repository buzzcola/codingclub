translator = str.maketrans(
    'abcdefghijklmnopqrstuvwxyz',
    'nopqrstuvwxyzabcdefghijklm'
)

message = input('What is the secret message?')
secret_code = str.translate(message, translator)
print(secret_code)
