# onji-simple-wizard
A simple multi step form wizard

## Getting started
```bash
$ flask run
```

## Application Structure
```
.
├── app.py                          # Flask Server
├── config.py                       # Server configuration settings
├── route.py                        # Route definition for serving wapp files
│
├── index.html                      # Index/Home page
├── js
│   ├── onji-simple-wizard.js       # The wizard code
│   └── main.js                     # Javascript file for index page
├── css
│   ├── onji-simple-wizard.css      # Stylesheet for wizard
│   └── main.css                    # Stylesheet for index page
├── views                           # Wizard partial views/htmls
│   ├── wizard-first-page.html
│   ├── wizard-second-page.html
│   └── wizard-third-page.html
└── images                          # Static images
```

## TODO
1. Remove dependency on jquery
2. Use partial views directly in index.html instead of relying on server to fetch
3. Remove hardcoded css classes in the wizard and use from params