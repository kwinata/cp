problem=$1
count=$2

for i in `seq 1 $count`
do
    infile="${problem}_${i}.in"
    outfile="${problem}_${i}.out"
    touch "${infile}"
    touch "${outfile}"
done
