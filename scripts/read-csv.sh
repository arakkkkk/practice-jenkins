# !/bin/bash
# read-csv.sh csv.csv

ARRAY=()
while IFS=, read -a col
do
  ARRAY=(${ARRAY[@]} col)
done < $1

echo ${ARRAY[@]}
