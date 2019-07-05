from mailer import Message, Mailer

validations = (
    # Validation callable     # Error response
    (lambda s: '@' in s,      "must have '@' in it"),
    (lambda s: len(s) > 6,    "is too short"),
    (lambda s: '.' in s,      "must have '.' in it")
)


def email_invalid(address):
    """Check address against a series of rules which must all pass.

      Returns an error string on failure; None on success.
        """
    for valid, error_message in validations:
        if not valid(address):
            return error_message


def check_email(email_address):
    while True:
        email_validity = email_invalid(email_address)
        if email_validity:
            email_address = raw_input(
                "Your email address '{}'\nPlease write your email address again: ".format(email_validity))
            continue
        else:
            return email_address


if __name__ == '__main__':
    message = Message()
    message.From = check_email(raw_input("From : "))
    message.To = check_email(raw_input("To : "))
    message.Body = raw_input("Body : ")
    message.Html = raw_input("HTML : ")
    message.Subject = raw_input("Subject : ")
    mailer = Mailer(raw_input("SMTP or Outbound address : "))
    mailer.send(message)
