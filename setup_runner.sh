usacorun() {
        echo "Compiling $1.cpp"
        g++-11 $1.cpp -o $1.o
        echo "Execute $1.o"
        ./$1.o
        echo "Printing $1.out"
        cat $1.out
}

comp() {
        echo "Compiling $1.cpp"
        g++-11 $1.cpp -Wall -o $1.o
}

ac() {
	echo "Compiling with Atcoder Library $1.cpp"
	CPLUS_INCLUDE_PATH="/Users/kevin.winata/workspace/ac-library" g++-11 $1.cpp -Wall -o $1.o
}

run() {
	echo "Running $1.cpp"
	./$1.o
}
