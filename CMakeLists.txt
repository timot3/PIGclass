cmake_minimum_required(VERSION 3.15)
project(PIGclass)

set(CMAKE_CXX_STANDARD 17)

add_executable(PIGclass main.cpp MainNode.cpp MainNode.hpp SubNode.cpp SubNode.hpp DisjointSet.cpp DisjointSet.hpp)