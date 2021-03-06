#!/usr/bin/env python3
import emails
import os
import reports


table_data = [
    ['Name', 'Amount', 'Value'],
    ['elderberries', 10, 0.45],
    ['figs', 5, 3],
    ['apples', 4, 2.75],
    ['durians', 1, 25],
    ['bananas', 5, 1.99],
    ['cherries', 23, 5.80],
    ['grapes', 13, 2.48],
    ['kiwi', 4, 0.49]]

# reports.generate("/tmp/report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)

reports.generate("C:\\Users\\jcste\\googleAutomation\\pyAutomate\\pyCarFigures\\report.pdf", "A Complete Inventory of My Fruit",
                 "This is all my fruit.", table_data)

# sender = "sender@example.com"
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."

# message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
message = emails.generate(sender, receiver, subject, body,
                          "C:\\Users\\jcste\\googleAutomation\\pyAutomate\\pyCarFigures\\report.pdf")
emails.send(message)
