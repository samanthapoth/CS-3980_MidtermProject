# FastAPI Sports App
This app was created for CS:3980:001 as a midterm project. The source code is from https://github.com/changhuixu/CS3980-2024/tree/main/my_todo_app. The function of this app is to allow users to add their NCAA favorite sports teams to a list. Any NCAA team can be chosen and the user can input what gender and what sport they like to follow. This app will be expanded to include stats of each team that the user adds, ticket sales of each team, and a new design interface for the user. Read teh information below to know how to properly run the app and use its features.

## 1. Python virtual environment

Windows:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

```powershell
deactivate
```

MacOS:
```powershell
source venv\bin\activate
```

```powershell
deactivate
```

## 2. pip

Pip is automatically installed during a Python installation. You can verify whether pip is
installed by running the following command in your terminal:

```powershell
python -m pip list
```

The preceding command should return a list of packages installed.

### Basic commands

To install the FastAPI package with pip, we run the following command:

```powershell
pip install fastapi
```

On a Unix operating system, such as Mac or Linux, in some cases, the sudo keyword is
prepended to install global packages.

To uninstall a package, the following command is used:

```powershell
pip uninstall fastapi
```

To collate the current packages installed in a project into a file, we use the following
freeze command:

```powershell
pip freeze > requirements.txt
```

The > operator tells bash to save the output from the command into the
`requirements.txt` file. This means that running pip freeze returns an output of
all the currently installed packages.

To install packages from a file such as the `requirements.txt` file, the following
command is used:

```powershell
pip install -r requirements.txt
```

The preceding command is mostly used in deployment.

## uvicorn

We'll begin by installing the dependencies required for our application in the todos
folder we created earlier. The dependencies are the following:

- fastapi: The framework on which we'll build our application.
- uvicorn: An Asynchronous Server Gateway Interface module to run our application.

First, activate your development environment by running the following command in your
project directory:

```powershell
source venv/bin/activate
```

Then, install the dependencies as follows:

```powershell
(venv)$ pip install fastapi uvicorn
```

The next step is to start our application using uvicorn. In your terminal, run the
following command:

```powershell
(venv)$ uvicorn main:app --port 8000 --reload
```

In the preceding command, uvicorn takes the following arguments:

- `file:instance`: The file containing the instance of FastAPI and the name
  variable holding the FastAPI instance.
- `--port PORT`: The port the application will be served on.
- `--reload`: An optional argument included to restart the application on every
  file change.

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install fastapi uvicorn
# pip freeze > requirements.txt
pip freeze | Out-File -Encoding UTF8 requirements.txt

# pip uninstall -r requirements.txt -y
```

## 3. Additional Files
The team_colors.json and sports.png files are added to this project to enhance user experience. 

The team_colors.json file attached contains the NCAA schools and hexcodes for their team colors. This file was obtained from
the following link:
https://www.kaggle.com/datasets/coreymaxedon/ncaa-team-color?resource=download

The owner and author Corey Maxedon created a csv with the above information. This file was converted to a json document using the following online conversion website.
https://www.convertcsv.com/csv-to-json.htm

The json file is used to populate the team name section on the sports team form to add or edit a team. 

The sports.png icon was used to change the icon on the header of the browser page while using the app. It was obtained from the following link:
https://www.flaticon.com/free-icon/sports_857418?term=sports&related_id=857418

The icon was created by Pause08 on Flaticon.

## 4. Using the App

To run the app, activate your virtual environment in you IDE as shown in #1 above. After that, navigate using the 'cd' command to the folder where your project is stored. Then, paste the following command in your terminal:

uvicorn main:app --port 8000 --reload

When the steps above are the completed, the app will open your web browser with the setup shown in the image below.

[App setup when app is opened](<Screenshot 2024-03-08 at 8.15.46 PM.png>)

To add a new team, press the "Add New Sports Team" button. This will bring up a form shown in the image below.

![Form used to create a new team](<Screenshot 2024-03-08 at 8.28.25 PM.png>)

Users must select crom the dropdown the name of the NCAA team they follow and what gender of sports they will be following. The Sport description box is optional for users to input what specific sport they would like to follow. Click the "Add" button to add the team to your list.

To edit the Name, Gender, or Sport of a team that you have added, click the edit button shown in the image below.

![Edit icon to edit a team](<Screenshot 2024-03-08 at 8.33.29 PM.png>)

Complete the form and click the "Update" button for changes to take effect.

To delete a team, click the trash can icon next ot the edit icon. This will permanently delete team from your app.

Enjoy using the app to track which NCAA teams you follow!