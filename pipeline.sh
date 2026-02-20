#!/bin/bash
echo "chunking data hit3.txt"
cat hitch3.txt | python3 chonk.py
ls part* | xargs -n 1 -P 4 cat | python3 mapper.py | sort | python3 reducer.py > out
echo "Output generated in out"
#less out