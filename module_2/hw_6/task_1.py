class Email:
    tld_list = ["com", "org", "net", "gov", "edu", "mil", "int", "aero", "museum", "coop", "info", "jobs", "mobi",
                "name", "pro", "travel", "asia", "cat", "tel", "xxx", "io", "app", "dev", "blog", "site", "online",
                "store", "tech", "xyz", "club", "media", "world", "space", "edu", "store", "shop", "studio", "design",
                "art", "me", "us", "uk", "ca", "au", "in", "de", "fr", "jp", "cn", "ru", "br", "es", "it", "nl", "se",
                "no", "fi", "dk", "ch", "at", "be", "pl", "cz", "hu", "gr", "tr", "pt", "ua", "ro", "sk", "nz", "za"]

    def __init__(self, mail):
        self.mail = mail

    def validate(self):
        split_mail = self.mail.split("@")
        split_domain = split_mail[-1].split(".")
        if "@" in self.mail:
            if split_mail[0][-1] != "-":
                if ".." not in split_mail[0]:
                    if split_mail[0][0] != ".":
                        if "#" not in split_mail[0]:
                            if ".." not in split_mail[1]:
                                if "." in split_mail[-1]:
                                    if split_domain[-1] in Email.tld_list:
                                        if "#" not in split_domain[0]:
                                            return f"Your email '{self.mail}' is valid!"
                                        else:
                                            return f"Your email '{self.mail}' has '#' before top-level domain"
                                    else:
                                        return f"Your top-level domains of your email '{self.mail}' isn't correct"
                                else:
                                    return f"Your email '{self.mail}' hasn't '.' after '@'"
                            else:
                                return f"Your email '{self.mail}' has '..' after '@'"
                        else:
                            return f"Your email '{self.mail}' has '#' before '@'"
                    else:
                        return f"Your email '{self.mail}' has '.' before email"
                else:
                    return f"Your email '{self.mail}' has '..' before '@'"
            else:
                return f"Your email '{self.mail}' has '-' before '@'"
        else:
            return f"Your email '{self.mail}' hasn't '@'"


email_1 = Email("maxim-@gmail.com")
email_2 = Email("max..im@gmail.com")
email_3 = Email(".maxim@gmail.com")
email_4 = Email("max#im@gmail.com")
email_5 = Email("maxim@gmail#it.com")
email_6 = Email("maxim@gmail")
email_7 = Email("maxim@gmail..com")
email_8 = Email("maxim@gmail.c")
true_email = Email("maxim@gmail.com")
print(email_1.validate())
print(email_2.validate())
print(email_3.validate())
print(email_4.validate())
print(email_5.validate())
print(email_6.validate())
print(email_7.validate())
print(email_8.validate())
print(true_email.validate())
