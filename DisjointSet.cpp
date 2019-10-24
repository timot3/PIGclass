//
// Created by Justin Wang on 10/19/2019.
//

#include "DisjointSet.hpp"

DisjointSet::DisjointSet(int n)  {
    for (int i = 0; i < n; i++) {
        set.push_back(-1);
    }
}

int DisjointSet::find(int a) {
    if (set[a] < 0) {
        return a;
    } else {
        //Path compression
        int ret = find(set[a]);
        set[a] = ret;
        return ret;
    }
}

bool DisjointSet::join(int a, int b) {
    int parA = find(a);
    int parB = find(b);
    if (parA == parB) {
        return false;
    } else {
        //Ranking
        if (size(a) < size(b)) {
            set[parB] += set[parA];
            set[parA] = parB;
        } else {
            set[parA] += set[parB];
            set[parB] = parA;
        }
        return true;
    }
}

bool DisjointSet::size(int a) {
    return -1 * set[find(a)];
}

