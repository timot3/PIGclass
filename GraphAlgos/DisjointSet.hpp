//
// Created by Justin Wang on 10/19/2019.
//

#ifndef PIGCLASS_DISJOINTSET_H
#define PIGCLASS_DISJOINTSET_H

#include<vector>

class DisjointSet {
public:
    std::vector<int> set;

    explicit DisjointSet(int n);

    int find(int a);

    bool join(int a, int b);

    bool size(int a);
};


#endif //PIGCLASS_DISJOINTSET_H
