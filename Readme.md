# Spiegel-data-fetching

- [Useful Snippets](#useful-snippets)
- [Depends on](#depends-on)
- [Setup (Linux)](#setup-linux)

### Useful snippets

```sh
# gets number of files in currrent dir
find . -type f | wc -l
```

```sh
# gets size of current dir
du -hs
```

```sh
# gets last modified files in current dir
find . -printf '%T+ %p\n' | sort -r | head
```

### Depends on

- `python3`
- `urllib3`
- `json`
- `os`
- `datetime`
- `glob`
- `BeautifulSoup`
- `re`
- `feedparser`

for analytics

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `networkx`

### Setup (Linux)

```sh
mkdir ~/apps
cd ~/apps
```

```sh
git clone https://github.com/emilianscheel/Spiegel-data-fetching
```

```sh
# Create system service
sudo nano /etc/systemd/system/spiegel-data-fetching.service
```

1. Replace `<user>` with your username
2. Paste the configuration into the file ends with `.service`

```
[Unit]
Description=Spiegel data fetching
After=multi-user.target
Wants=spiegel-data-fetching.timer

[Service]
Type=oneshot
WorkingDirectory=/home/<user>/apps/Spiegel-data-fetching/
ExecStart=/usr/bin/python3 main.py

[Install]
WantedBy=multi-user.target
```

```sh
# Create system timer
sudo nano /etc/systemd/system/spiegel-data-fetching.timer
```

1. Replace `<user>` with your username
2. Paste the configuration into the file ends with `.timer`

```
[Unit]
Description=Fetches Spiegel.de for data and saves it
Requires=spiegel-data-fetching.service

[Timer]
Unit=spiegel-data-fetching.service
OnCalendar=*:0/11

[Install]
WantedBy=timers.target
```

```sh
# starts and enables service, view status
sudo systemctl enable spiegel-data-fetching.service
sudo systemctl start spiegel-data-fetching.service
sudo systemctl status spiegel-data-fetching.service

# starts and enables timer, view status
sudo systemctl enable spiegel-data-fetching.timer
sudo systemctl start spiegel-data-fetching.timer
sudo systemctl status spiegel-data-fetching.timer
```

That configuration starts our system service every eleven minutes. The system service triggers the `main.py` script which is the fetching a spiegel rss feed.
