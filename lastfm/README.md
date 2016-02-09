# lastfm.py

Pull last song played from [Last.fm](https://www.last.fm) and write to stdout, which is where [TextExpander](https://smilesoftware.com/textexpander) accepts it.

**Requirements**:

- Python
- Requests module (for Python)
- Last.fm account with API access, API key is required

**Usage**:

1. Ensure [Requirements] are met.
1. Copy lastfm.py to some location on your system, note path to same.
1. Create new snippet in TextExpander, set as type `Shell Script`
1. Add an appropriate Label, e.g. `Now Playing`
1. Add your desired Abbreviation, e.g. `,,np`
1. Add the code, changing the paths to reflect both the location of the file, and of the `python` interpreter:

    ```bash
    #!/bin/bash
    
    LASTFM_USER=your_user \
    LASTFM_KEY=your_key \
    /usr/local/bin/python \
    /Users/username/Dropbox/Apps/TextExpander/scripts/lastfm.py 
    ```

1. Test it out by typing `,,np` in your favorite text editor

Good Luck!

