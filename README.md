# pyastf-json-convertor
Converts a python astf profile to json for use with jsrex

## What is this?
It reads in a python astf profile, and stdout's the converted json.

## Why?
For use with jsrex library (or your own zmq interface to trex)

## How to use?
```
git clone --recursive https://github.com/velocipacktor/pyastf-json-convertor.git
cd pyastf-json-convertor
mkdir output
./convertor.py trex-core/scripts/astf/http_simple.py | tee output/http_simple.json
cat output/http_simple.json
```
