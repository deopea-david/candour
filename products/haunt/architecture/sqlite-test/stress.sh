#!/bin/bash
# stress.sh <label> <K> <n> <runner...>   runner gets: libA libB dir n "5"
label=$1; K=$2; n=$3; shift 3
D=/private/tmp/claude-501/-Users-davidparrish-Documents-candour/1c0db2a6-d671-472b-91d8-5123d15bad48/scratchpad/sqlite-test
crash=0; lost=0; corrupt=0; clean=0; other=0
for i in $(seq 1 $K); do
  dir=$D/stress/$label/$i; rm -rf $dir; mkdir -p $dir
  out=$("$@" $dir $n 5 2>&1); rc=$?
  exp=$(echo "$out" | sed -n 's/.*rows that should exist: \([0-9]*\).*/\1/p')
  got=$(/usr/bin/sqlite3 $dir/t5.db "select count(*) from t" 2>&1)
  ic=$(/usr/bin/sqlite3 $dir/t5.db "pragma integrity_check" 2>&1 | tr '\n' ' ' | cut -c1-120)
  if [ $rc -ne 0 ]; then res="CRASH(rc=$rc)"; crash=$((crash+1));
  elif [ "$ic" != "ok " ]; then res="CORRUPT"; corrupt=$((corrupt+1));
  elif [ "$got" != "$exp" ]; then res="LOST $((exp-got)) of $exp committed rows"; lost=$((lost+1));
  else res="clean"; clean=$((clean+1)); fi
  if [ $rc -ne 0 ] && [ "$ic" != "ok " ]; then corrupt=$((corrupt+1)); res="$res + CORRUPT"; fi
  echo "  run $i: $res | rows=$got expected=${exp:-n/a} | integrity: $ic"
done
echo "SUMMARY $label: K=$K n=$n/thread  clean=$clean crash=$crash lost=$lost corrupt=$corrupt"
