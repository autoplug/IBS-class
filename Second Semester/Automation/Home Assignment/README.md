# MIB Automation Home Assignment

## First Step : Install Dependency

I listed all of dependency in a file. Install dependency by run code below:

```
pip install -r requirements.txt
```

## Second Step

If you run the app.py, you can see it create a "TopRanks" spreadsheet in google drive and a script file.

you need to run script one and get the permissions.

You do not need to do anything.It create spreadsheet in google drive and every month that code run based on scheduale it create new form and save the response of form inside a spreadsheet. You can see average and every vote in detail.

## Last Step Scheduling

in crontab -e add command below:

```
0 0 1 \* \* python3 app.py
```
