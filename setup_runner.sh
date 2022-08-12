cpprun() {
        echo "Compiling $1.cpp"
        g++ -std=c++11 $1.cpp -o $1.o
        echo "Execute $1.o"
        ./$1.o
        echo "Printing $1.out"
        cat $1.out
}