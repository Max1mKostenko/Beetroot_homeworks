import string
from mail_def import generator_of_emails

generator_of_emails(["gmail", "yahoo", "hotmail", "outlook", "microsoft", "example", "domain", "test", "mail", "abc",
                     "google", "apple", "amazon", "facebook", "twitter", "linkedin", "reddit", "stackoverflow"],

                    [".com", ".ua", ".fr", ".net", ".org", ".gov", ".us", ".uk", ".de", ".es"],

                    list(string.ascii_letters + string.digits),

                    input("Please enter the quantity of mails to generate: "))
