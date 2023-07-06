import random


def generator_of_emails(domains, domain_zones, name_domain, quantity_mails):
    try:
        quantity_mails = int(quantity_mails)
        if quantity_mails > 0:
            for i in range(quantity_mails):
                if i == 0:
                    print(f"{i + 1}st email: {''.join(random.choices(name_domain, k=random.randint(8, 17)))}"
                          f"@{random.choice(domains)}{random.choice(domain_zones)}")
                elif i == 1:
                    print(f"{i + 1}nd email: {''.join(random.choices(name_domain, k=random.randint(8, 17)))}"
                          f"@{random.choice(domains)}{random.choice(domain_zones)}")
                elif i == 2:
                    print(f"{i + 1}rd email: {''.join(random.choices(name_domain, k=random.randint(8, 17)))}"
                          f"@{random.choice(domains)}{random.choice(domain_zones)}")
                else:
                    print(f"{i + 1}th email: {''.join(random.choices(name_domain, k=random.randint(8, 17)))}"
                          f"@{random.choice(domains)}{random.choice(domain_zones)}")
        else:
            print(f"Your input is number: {quantity_mails}. You must enter a number that is more than 0.")
    except ValueError:
        print(f"Your input: '{quantity_mails}', isn't correct. You should enter a valid number greater than 0.")
