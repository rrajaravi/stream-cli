# stream-cli

https://getstream.io/

https://pypi.org/project/stream-cli/

CLI for activity feed APIs 

###  Getting it

To download, either fork this github repo or simply use Pypi via pip.
```sh
$ pip install stream-cli
```

### Using it

```
Usage: stream_cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  -k, --api-key TEXT     getstream.io api key  [required]
  -s, --secret-key TEXT  getstream.io secret key  [required]
  -l, --location TEXT    getstream.io hosted location
  --help                 Show this message and exit.

Commands:
  delete-activity-from-feed
  delete-all-activity-from-feed
  get-activities-from-feed
  get-followers
  get-notification-by-id
  remove-activity
  update-mark-seen
 ```
