% imp.py(1) Version 1.0 | imp.py

# NAME
imp.py - a generic template for my cool program

# SYNOPSIS
**imp.py** [*options*] [*args*]

# DESCRIPTION
**imp.py** is a command-line utility that attempts to automate a lot of the manual implementation process post portal entry.

# OPTIONS
**--create-decoder-confs** ENDPOINT
:   Create OU decoderX.conf files for all OU decoders at the specified endpoint.

**--update-leaf --csv** CSV_FILE
:   Update specific parts of a leaf in a 2 column csv. Column 1 should always be "leaf_id" column 2 should be whatever
:   value needs to be changed ie. "description", "status", "multicast_handoff" etc.

**--update-flowclient --csv** CSV_FILE
:   Update specific parts of a flowclient in a 2 column csv. Column 1 should always be "flowclient_id" column 2 should be whatever
:   value needs to be changed ie. "description", "status", "multicast_handoff" etc same as --update-leaf but for flowclients.

**--rename-leaf --csv CSV_FILE**
:   Rename a leaf in the portal. Column 1 should be the current "leaf_id" to be changed. Column 2 should be the new "leaf_id"
# EXAMPLES

Run the program with a specific config:

    $ imp.py --create-decoder-confs ltnr-bwi-rcollins

    $ imp.py --update-leaf --csv <PATH TO CSV FILE>

# BUGS
See GitHub Issues: <https://github.com/darthmegatron/imp/issues>

# AUTHOR
Robert Collins <randomhuman-rc@proton.me>
