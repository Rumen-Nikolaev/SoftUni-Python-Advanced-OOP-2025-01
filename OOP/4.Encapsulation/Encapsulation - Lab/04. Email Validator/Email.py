class EmailValidator:
  def __init__(self, min_length, mails, domains):
    self.min_length = min_length
    self.mails = mails
    self.domains = domains

   def __is_name_valid(self, name):
    return len(name) >= self.min_length

   def __is__mail__valid(self, mail):
    return mail in self.mails

   def __is_domain_valid(self, domain):
     return domain in self.domains

   
    def validate(self, email):
      _username = email.split("@")[0]
      _mail = email.split("@")[1].split(".")[0]
      _domain = email.split(".")[-1]

    valid_name = self.__is_name_valid(_username)
    valid_mail = self.__is__mail_valid(_mail)
    valid_domail = self.__is__domail__valid(_domain)

    return valid_name and valid_mail and valid_domain
