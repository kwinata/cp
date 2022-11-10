: '

# How to setup:

`source ./tester.sh` to register the commands


# How to use:

>> `maketest abc084b 5`

This will create 10 files:
abc084b_1.in
abc084b_1.out
abc084b_2.in
abc084b_2.out
abc084b_3.in
abc084b_3.out
abc084b_4.in
abc084b_4.out
abc084b_5.in
abc084b_5.out


>> `runtest python3 abc084b py`

This will run the test cases


>> `cleantest abc084b`

This will delete all the files


'


maketest() {
    problem=$1
    count=$2

    for i in `seq 1 $count`
    do
        infile="${problem}_${i}.in"
        outfile="${problem}_${i}.out"
        touch "${infile}"
        touch "${outfile}"
    done
}

runtest() {
    runner=$1
    problem=$2
    filext=$3

    commandexec="${runner}"
    progfile="${problem}${filext}"
    for i in {1..20}
    do
        infile="${problem}_${i}.in"
        outfile="${problem}_${i}.out"
        outtmp="${problem}_${i}.out_tmp"

        if [ -f "${infile}" ] && [ -f "${outfile}" ] ; then
        
            echo "Running test case ${i}"

            cat "${infile}" | $commandexec "${progfile}" > $outtmp
            diff -B $outfile $outtmp  > /dev/null 2>&1
            error_code=$?  # get diff command exit code            
            if [[ $error_code != 0 ]]; then 
                echo "\n!!! Output differs:\n"
                diff -B $outfile $outtmp

                echo "\nFull file:"
                echo "-----\nExpected: (${outfile})"
                cat "${outfile}"

                echo "\n-----\nActual:"
                cat "${outtmp}"
            else 
                echo "OK"
            fi

            rm "${outtmp}"

            if [[ $error_code != 0 ]]; then 
                return $error_code 
            fi  

        else
            echo "${infile} or ${outfile} is not found" 
            echo "Finish running"
            return
        fi
    done
}

cleantest() {
    problem=$1

    for i in {1..20}
    do
        infile="${problem}_${i}.in"
        outfile="${problem}_${i}.out"

        if [ -f "${infile}" ] || [ -f "${outfile}" ] ; then
            echo "Deleting ${infile}" 
            rm "${infile}"
            echo "Deleting ${outfile}"
            rm "${outfile}"
        else
            echo "${infile} or ${outfile} is not found" 
            echo "Finish running"
            return
        fi
    done
}
