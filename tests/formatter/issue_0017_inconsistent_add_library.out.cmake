add_library(
    foo
    INTERFACE
    include/File1.hpp
    include/File2.hpp
    include/File3.hpp
    include/File4.hpp
    include/File5.hpp
)

add_library(
    foo
    SHARED
    src/File1.cpp
    src/File2.cpp
    src/File3.cpp
    src/File4.cpp
    src/File5.cpp
)

add_library(FOO INTERFACE foo bar baz)

add_library(
    FOO
    INTERFACE
    long_arg____________________________________________________________
    long_arg____________________________________________________________
    long_arg____________________________________________________________
)

add_library(FOO INTERFACE EXCLUDE_FROM_ALL foo bar baz)

add_library(
    FOO
    INTERFACE
    EXCLUDE_FROM_ALL
    long_arg____________________________________________________________
    long_arg____________________________________________________________
    long_arg____________________________________________________________
)
