#!/bin/bash
# get.sh <pref> <zmenseni> n1 n2 ... -> /home/user/Rodokmen/pracovni/<pref>/s<n>_q.jpg (2) nebo s<n>.jpg (0)
pref=$1; z=$2; shift 2; D=/home/user/Rodokmen/pracovni/$pref; mkdir -p $D
cd /tmp/claude-0/-home-user/c5abcc80-15f6-5483-acee-86603357c514/scratchpad/pw
need=""; for n in "$@"; do grep -q "^$n	" $D/cesty.tsv 2>/dev/null || need="$need $n"; done
[ -n "$need" ] && NODE_PATH=$(npm root -g) node pth.js $pref $need >> $D/cesty.tsv
cd /home/user/Rodokmen
for n in "$@"; do u=$(awk -v n=$n '$1==n{print $2; exit}' $D/cesty.tsv); suf=$([ $z = 0 ] && echo "" || echo "_q"); [ -f $D/s${n}${suf}.jpg ] || python3 -I tools/soal_zoomify.py "$u" $z $D/s${n}${suf}.jpg | tail -1; done
