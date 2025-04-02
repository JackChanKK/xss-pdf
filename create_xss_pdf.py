# -*- coding:utf-8 -*-

if __name__ == "__main__":
  with open("D://playwright/xssPDF-test1.pdf", "w") as file:
    file.write('''%PDF-1.7
    1 0 obj
    <</Pages 1 0 R /OpenAction 2 0 R>>
    2 0 obj
    <</S /JavaScript /JS (app.alert('POC test for xss pdf.'))>> 
    trailer
    <</Root 1 0 R>>''')
