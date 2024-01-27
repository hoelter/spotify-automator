# Spotify Playlist Backup Script

This is python script/project that is designed to run at certain times to backup the discover weekly and release radar playlists on spotify.

There is a bash script which sets up a cronjob for this python script to run every Monday and Friday, creating a copy of the latest discover weekly/release radar playlist and putting the date in the copies name.

To get this setup:

1) Create a .env file with 3 values set
```
SPOTIPY_CLIENT_SECRET=<client secret here>
SPOTIPY_CLIENT_ID=<client id here>
SPOTIPY_REDIRECT_URI=http://localhost/
```


## Install System Dependencies

- Apt dependencies `sudo apt install pipx`
- Poetry package manager `pipx install poetry`

## Setup Project Dependencdies

- In the root directory of the project, install the packages with poetry `poetry install --no-root`


## How to Execute the script using poetry

- Run `poetry run python3 backup-weekly-playlists.py`

## Install Cron Job to auto execute the Script

- This cron job runs the script at 9am on Monday to backup the Discover Weekly playlist and 9 am on Friday to backup the Release Radar playlist.
- Make sure the crontab isn't empty, and then execute the script in this project `./install-backup-cron-job`
- Check that it installed correctly using `crontab -l`, and if it looks off (the poetry executable or this project directory path is incorrect) either manually edit it using `crontab -e` or just try running the install script again.
