import outlook
mail = outlook.Outlook()
mail.login('uhlir@outlook.cz','babicKa+1934/')
mail.inbox()
print(mail.unread())