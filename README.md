# Assaydashboard

A Dashboard application built using django and chart.js

## Data requirements
1. The uploaded CSV files must contain be in the following format.

| Assay                                     | January | November | December | Year | AssayID       | MachineID           |
| :---------------------------------------: | :-----: | :------: | :------: | :--: | :-----------: | :-----------------: |
| Sick panel (MS/MS)                        | 279     | 219      | 220      | 2020 | SICKPANEL\_20 | FI-MSMS             |
| Urine organic Acid (UOA)                  | 119     | 101      | 127      | 2020 | UOA\_20       | GC-MS               |
| Plasma Amino Acid (PAA)                   | 69      | 0        | 5        | 2020 | PAA\_20       | Amino acid analyzer |
| Plasma Very Long Chain Fatty Acid (VLCFA) | 28      | 48       | 54       | 2020 | VLCFA\_20     | LC-MSMS-1           |
| Serum Methyl Maalonic Acid (MMA)          | 44      | 44       | 40       | 2020 | MMA\_20       | LC-MSMS-2           |
| Serum Biotinidase                         | 16      | 11       | 36       | 2020 | SERUM\_20     | Spectrophotometer   |

2. The month names must be in full title format. (first letter must be capital) 
3. The assayID and machineID must be unique. and the ID must the 2 digit year for the corresponding data.
4. The app is designed such that the user uploads the sample collected data every month, for the same ASSAYID's.  
## ✨ Deploy in production using `Docker`

> Get the code

```bash
$ git clone <repo>
$ cd genelookup
```
> Configure environment variables
```
1. Create a .env file and paste the contents. 

DEBUG=1
DB_NAME=dbname
DB_USER=rootuser
DB_PASS=changeme
SECRET_KEY=changeme
ALLOWED_HOSTS=127.0.0.1

2. Change the variables to store real values.
3. Allowed hosts can be a comma seperated list of multiple hosts (IP's or domain names)
```
> Start the app in Docker

```bash
$ docker-compose up --build
$ docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

Visit `http://localhost:80` in your browser. The app should be up & running.


<br />

## ✨ How to use it for development
The development deployment provies hot reloading for the code to update in real time
```bash
$ # Get the code
$ git clone <repo>
$ cd genelookup
$
$ 
$ # Docker compose
$ docker-compose -f docker-compose-dev.yml up --build
$
$ # open a new terminal and run 
$ docker-compose -f docker-compose-dev.yml run --rm app sh -c "python manage.py createsuperuser"
$
$ # Access the web app in browser: http://127.0.0.1/
```

<br />

## Code-base structure

The project is coded using a simple and intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## ✨ Recompile CSS

To recompile SCSS files, follow this setup:

<br />

**Step #1** - Install tools

- [NodeJS](https://nodejs.org/en/) 12.x or higher
- [Gulp](https://gulpjs.com/) - globally 
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/) (optional) 

<br />

**Step #2** - Change the working directory to `assets` folder

```bash
$ cd apps/static/assets
```

<br />

**Step #3** - Install modules (this will create a classic `node_modules` directory)

```bash
$ npm install
// OR
$ yarn
```

<br />

**Step #4** - Edit & Recompile SCSS files 

```bash
$ gulp scss
```

The generated file is saved in `static/assets/css` directory.

<br />

## Future improvement proposals
1. Better way of handling header row in csv files
2. Allowing users to upload profile pic 

## ✨ Credits & Links

- [Django](https://www.djangoproject.com/) - The official website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

<br />

---
[Django Bootstrap 5](https://appseed.us/admin-dashboards/django-dashboard-volt) Volt - Provided by **AppSeed [App Generator](https://appseed.us/app-generator)**.
